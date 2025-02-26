from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

    PROFILE_TYPES = [
        ('business', 'Geschäftsprofil'),
        ('customer', 'Kundenprofil'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    file = models.FileField(upload_to=None)
    location = models.CharField(max_length=200)
    tel = models.IntegerField(null=True)
    description = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=PROFILE_TYPES)
    created_at = models.CharField(max_length=200)