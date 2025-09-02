from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect
from functools import wraps
import jwt
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from django.http import HttpResponseRedirect


def jwt_login_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        access_token = request.COOKIES.get('access')
        refresh_token = request.COOKIES.get('refresh')  

        if not access_token:
            print("No access token. Checking refresh token...")
            if not refresh_token:
                print("No refresh token. Redirecting to login.")
                return redirect('login')

            try:
                # Decode refresh token to validate it
                payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=["HS256"])
                print("Refresh token is valid. You could now issue a new access token.")
                
                # Optional: Automatically generate a new access token here
                # Or redirect to a refresh endpoint
                request.user_id = payload['user_id']
            except (ExpiredSignatureError, InvalidTokenError):
                print("Refresh token is invalid or expired.")
                return redirect('login')
        else:
            try:
                payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=["HS256"])
                request.user_id = payload['user_id']
            except (ExpiredSignatureError, InvalidTokenError):
                print("Access token invalid. Checking refresh token...")
                if not refresh_token:
                    return redirect('login')
                try:
                    payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=["HS256"])
                    request.user_id = payload['user_id']
                except:
                    return redirect('login')

        return func(request, *args, **kwargs)
    return wrapper

@never_cache
def login_view(request):
    return render(request, 'login.html')

@never_cache
def register_view(request):
    return render(request, 'register.html')

@never_cache
# @jwt_login_required
def dashboard_view(request):
    return render(request, 'index.html')

@never_cache
# @jwt_login_required
def change_password_page(request):
    return render(request, 'change_password.html')

@never_cache
# @jwt_login_required
def profile_view(request):
    return render(request, "profile.html")
