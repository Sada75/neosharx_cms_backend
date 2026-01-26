from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
import uuid


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)

        if not password:
            raise ValueError("Superusers must have a password")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    AUTH_PROVIDERS = (
        ("local", "Local"),
        ("google", "Google"),
        ("linkedin", "LinkedIn"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150)

    # Auth
    auth_provider = models.CharField(
        max_length=20, choices=AUTH_PROVIDERS, default="local"
    )
    google_id = models.CharField(max_length=255, blank=True, null=True)
    linkedin_id = models.CharField(max_length=255, blank=True, null=True)

    # Profile
    avatar_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    # Admin
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
