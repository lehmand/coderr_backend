from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):

    business_user = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewer = models.IntegerField()
    rating = models.IntegerField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
    

