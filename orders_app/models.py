from django.db import models
from offers_app.models import Offer

# Create your models here.
class Order(models.Model):

    customer_user = models.IntegerField()
    business_user = models.IntegerField()
    title = models.CharField(max_length=200)
    revisions = models.IntegerField()
    delivery_time_in_days = models.IntegerField()
    price = models.IntegerField()
    features = models.CharField(max_length=200)
    offer_type = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default='in_progress')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
