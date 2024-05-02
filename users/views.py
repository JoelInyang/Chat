# users/views.py
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
#from django.utils.encoding import smart_str, force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import SignUpSerializer

class Signup(APIView):
    def post(self, request, format=None):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Create a JWT refresh token
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)

            return Response(
                {
                    "message": "User created successfully.",
                    "statuscode": 201,
                    "token": token  # Include the token in the response
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "message": "Invalid Input",
                "statusCode": 400,
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class Login(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"message": "Unsuccessful, kindly re-enter your credentials", "status" : 404}, status=status.HTTP_404_NOT_FOUND
            )

        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)

            return Response(
                {
                    "message": "User authenticated successfully",
                    "statusCode": 200,
                    "token": token,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Unsuccessful, kindly re-enter your credentials", "status": 404},
                status=status.HTTP_404_NOT_FOUND
            )
