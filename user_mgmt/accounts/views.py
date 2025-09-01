from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import UserRegisterSerializer, ProfileSerializer, PasswordChangeSerializer

# Register
@api_view(["POST"])
@permission_classes([AllowAny])
def register_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"detail": "User registered"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Login (function-based using TokenObtainPairSerializer)
# @api_view(["POST"])
# @permission_classes([AllowAny])
# def login_view(request):
#     serializer = TokenObtainPairSerializer(data=request.data)
#     try:
#         serializer.is_valid(raise_exception=True)
#     except Exception as e:
#         return Response({"detail": "Invalid credentials", "errors": serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)
#     return Response(serializer.validated_data, status=status.HTTP_200_OK)

# # Token refresh (function-based)
# from rest_framework_simplejwt.serializers import TokenRefreshSerializer

# @api_view(["POST"])
# @permission_classes([AllowAny])
# def token_refresh_view(request):
#     serializer = TokenRefreshSerializer(data=request.data)
#     try:
#         serializer.is_valid(raise_exception=True)
#     except Exception:
#         return Response({"detail": "Invalid refresh token"}, status=status.HTTP_401_UNAUTHORIZED)
#     return Response(serializer.validated_data, status=status.HTTP_200_OK)

# # Logout - blacklist refresh
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def logout_view(request):
#     refresh_token = request.data.get("refresh")
#     if not refresh_token:
#         return Response({"detail": "Refresh token required"}, status=status.HTTP_400_BAD_REQUEST)
#     try:
#         token = RefreshToken(refresh_token)
#         token.blacklist()
#     except Exception:
#         return Response({"detail": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
#     return Response({"detail": "Logged out"}, status=status.HTTP_205_RESET_CONTENT)

# Profile endpoints
@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def profile_view(request):
    profile = request.user.profile
    if request.method == "GET":
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # PUT (partial updates allowed)
    serializer = ProfileSerializer(profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Change password
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def change_password_view(request):
    serializer = PasswordChangeSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response({"detail": "Password changed"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
