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
    (SIXTH, "6th"),
    (SEVENTH, "7th"),
    (EIGHTH, "8th"),
    (MIDDLE, "Middle School (6th, 7th, 8th)"),
    (ALL, "All"),
]


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    grade = models.IntegerField(choices=grade_choices, default=ALL)

    TEACHER = "TEACHER"
    OFFICE_OR_SUBSTITUTE = "OFFICE_OR_SUBSTITUTE"
    OFFICE_ADMIN = "OFFICE_ADMIN"

    ROLE_CHOICES = [
        (TEACHER, "Teacher"),
        (OFFICE_OR_SUBSTITUTE, "Office or Substitute"),
        (OFFICE_ADMIN, "Office Administration"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=TEACHER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class ValidEmail(models.Model):
    email = models.EmailField(max_length=150)

    class Meta:
        verbose_name_plural = "Valid Emails"

    def __str__(self):
        return self.email
