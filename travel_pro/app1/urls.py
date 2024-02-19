# app1/urls.py

from django.urls import path
from .views import UserRegistrationView, UserLoginView, AdminRegistrationView, AdminLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('a/register/', AdminRegistrationView.as_view(), name='admin-register'),
    path('a/login/', AdminLoginView.as_view(), name='admin-login'),
]
