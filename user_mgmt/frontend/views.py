from django.views.decorators.cache import never_cache
from django.shortcuts import render

@never_cache
def login_view(request):
    return render(request, 'login.html')

@never_cache
def register_view(request):
    return render(request, 'register.html')

@never_cache
def dashboard_view(request):
    return render(request, 'index.html')

@never_cache
def change_password_page(request):
    return render(request, 'change_password.html')

@never_cache
def profile_view(request):
    return render(request, "profile.html")
