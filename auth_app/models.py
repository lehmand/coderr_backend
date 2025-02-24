from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):

    PROFILE_TYPES = (
        ('business', 'Geschäftsprofil'),
        ('customer', 'Kundenprofil'),
    )

    type = models.CharField(max_length=20, choices=PROFILE_TYPES)
