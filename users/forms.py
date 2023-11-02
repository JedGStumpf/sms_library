from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    PasswordResetForm,
)
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from .models import CustomUser


class SignInForm(AuthenticationForm):
    captcha = CaptchaField()


class CustomUserCreationForm(UserCreationForm):
    """
        Custom User Creation Form
        Used only by Admin
    """
    class Meta:
        model = CustomUser
        fields = ("email", "grade")


class NonAdminCustomUserCreationForm(UserCreationForm):
    """
        Custom User Creation Form
        Used only by common users
    """
    captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = ("email", "grade")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomPasswordResetForm(PasswordResetForm):
    captcha = CaptchaField()