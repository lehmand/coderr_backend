from django.db import models


# Create your models here.
class UserProfile(models.Model):

    PROFILE_TYPES = [
        ('business', 'Geschäftsprofil'),
        ('customer', 'Kundenprofil'),
    ]    

    type = models.CharField(max_length=20, choices=PROFILE_TYPES)


