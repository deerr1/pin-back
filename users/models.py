from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.FileField(verbose_name='Аватар', upload_to="avatar", blank=True, null=True, editable=True)