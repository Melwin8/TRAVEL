# # myapp/serializers.py

# from django.core.exceptions import ValidationError
# from rest_framework import serializers
# from .models import CustomUser

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         try:
#             user = CustomUser.objects.create_user(**validated_data)
#             return user
#         except ValidationError as e:
#             raise serializers.ValidationError({'error': str(e)})

# class AdminRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         try:
#             user = CustomUser.objects.create_admin_user(**validated_data)
#             return user
#         except ValidationError as e:
#             raise serializers.ValidationError({'error': str(e)})

# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(style={'input_type': 'password'})

#     def validate(self, data):
#         email = data.get('email')
#         password = data.get('password')

#         if email and password:
#             # Custom logic for validating the email and password
#             user = CustomUser.objects.filter(email=email).first()

#             if user and user.check_password(password):
#                 # Valid credentials
#                 data['user'] = user
#             else:
#                 raise serializers.ValidationError('Invalid email or password.')
#         else:
#             raise serializers.ValidationError('Both email and password are required.')

#         return data
    
# class AdminLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}


# serializers.py
from rest_framework import serializers
from .models import CustomUser, AdminUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','email', 'password')

class AdminRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = ('username','email', 'password')

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

class AdminLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
