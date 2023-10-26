from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    PasswordResetForm,
)
from captcha.fields import CaptchaField
from .models import CustomUser


class SignInForm(AuthenticationForm):
    captcha = CaptchaField()


class CustomUserCreationForm(UserCreationForm):
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