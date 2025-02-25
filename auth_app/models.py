from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):

    PROFILE_TYPES = [
        ('business', 'Geschäftsprofil'),
        ('customer', 'Kundenprofil'),
    ]    

    type = models.CharField(max_length=20, choices=PROFILE_TYPES)
