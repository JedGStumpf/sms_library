from django.db.models.signals import pre_save

# from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth import get_user_model
