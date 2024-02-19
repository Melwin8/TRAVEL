# myapp/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None, **extra_fields):
#         email = self.normalize_email(email)
#         if CustomUser.objects.filter(email=email).exists():
#             raise ValidationError(_('Email already exists'))
#         if CustomUser.objects.filter(username=username).exists():
#             raise ValidationError(_('Username already exists'))

#         user = self.model(email=email, username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_admin_user(self, email, username, password=None, **extra_fields):
#         email = self.normalize_email(email)
#         if CustomUser.objects.filter(email=email).exists():
#             raise ValidationError(_('Email already exists'))
#         if CustomUser.objects.filter(username=username).exists():
#             raise ValidationError(_('Username already exists'))

#         user = self.create_user(email, username, password, **extra_fields)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     date_joined = models.DateTimeField(default=timezone.now)

#     objects = CustomUserManager()

#     # Provide unique related names for groups and user_permissions
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='custom_user_groups',
#         blank=True,
#         verbose_name=_('groups'),
#         help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
#     )
    
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='custom_user_permissions',
#         blank=True,
#         verbose_name=_('user permissions'),
#         help_text=_('Specific permissions for this user.'),
#     )

#     def __str__(self):
#         return self.username

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.email
class AdminUserManager(BaseUserManager):
    def create_admin_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        admin_user = self.model(email=email, is_staff=True, **extra_fields)
        admin_user.set_password(password)
        admin_user.save(using=self._db)
        return admin_user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_admin_user(email, password, **extra_fields)

class AdminUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = AdminUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='admin_user_groups',
        blank=True,
        help_text='The groups this admin user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='admin_user_permissions',
        blank=True,
        help_text='Specific permissions for this admin user.',
    )

    def __str__(self):
        return self.email