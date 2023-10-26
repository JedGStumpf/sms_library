from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


KINDER = 0
FIRST = 1
SECOND = 2
THIRD = 3
FOURTH = 4
FIFTH = 5
SIXTH = 6
SEVENTH = 7
EIGHTH = 8
MIDDLE = 9
ALL = 10

grade_choices = [
    (KINDER, "Kinder"),
    (FIRST, "1st"),
    (SECOND, "2nd"),
    (THIRD, "3rd"),
    (FOURTH, "4th"),
    (FIFTH, "5th"),
    (SIXTH, "6th Only"),
    (SEVENTH, "7th Only"),
    (EIGHTH, "8th Only"),
    (MIDDLE, "Middle School - 2 or more of: (6th, 7th, 8th)"),
    (ALL, "All - For Substitutes and Office Staff Only"),
]


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    grade = models.IntegerField(choices=grade_choices, blank=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class ValidEmail(models.Model):
    email = models.EmailField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = "Valid Emails"

    def __str__(self):
        return self.email
