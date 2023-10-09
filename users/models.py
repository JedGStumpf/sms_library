from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


KINDER = "K"
FIRST = "1ST"
SECOND = "2ND"
THIRD = "3RD"
FOURTH = "4TH"
FIFTH = "5TH"
SIXTH = "6TH"
SEVENTH = "7TH"
EIGHTH = "8TH"
MIDDLE = "M"
ALL = "ALL"

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
    grade = models.CharField(max_length=35, choices=grade_choices, default=ALL)
    needs_reset_email = models.BooleanField(default=True)

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
