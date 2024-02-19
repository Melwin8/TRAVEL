from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserRegistrationSerializer, AdminRegistrationSerializer, UserLoginSerializer, AdminLoginSerializer
from .models import CustomUser , AdminUser

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        existing_user = CustomUser.objects.filter(email=email).first()

        if existing_user:
            return Response({'message': 'User with this email already registered. Please log in.'})

        response = super().create(request, *args, **kwargs)
        return Response({'message': 'User registration successful!'})

class AdminRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()  # Replace with AdminUser queryset
    serializer_class = AdminRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        existing_admin = AdminUser.objects.filter(email=email).first()

        if existing_admin:
            return Response({'message': 'Admin with this email already registered. Please log in.'})

        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Admin registration successful!'})

class UserLoginView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get('user')

        if user:
            token, created = Token.objects.get_or_create(user=user)
            response_data = {'token': token.key, 'message': 'Login successful! Welcome back.'}
            return Response(response_data)
        else:
            return Response({'message': 'Invalid email or password.'}, status=400)

class AdminLoginView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()  # Replace with AdminUser queryset
    serializer_class = AdminLoginSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'message': 'Admin login successful! Welcome back.'})
