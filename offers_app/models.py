from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Offer(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to=None, null=True, blank=True)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class OfferDetail(models.Model):

    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='details')
    title = models.CharField(max_length=200)
    revisions = models.PositiveIntegerField(default=0)
    delivery_time_in_days = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=100)
    features = models.CharField(max_length=200)
    offer_type = models.CharField(max_length=200)

    def __str__(self):
        return self.title