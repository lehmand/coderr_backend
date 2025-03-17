from django.db import models
from django.contrib.auth.models import User
from django.db.models import Min
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class Offer(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to=None, null=True, blank=True)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    min_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    min_delivery_time = models.PositiveIntegerField(default=7)
    

    def __str__(self):
        return self.title
    
class OfferDetail(models.Model):

    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='details')
    title = models.CharField(max_length=200)
    revisions = models.PositiveIntegerField(default=0)
    delivery_time_in_days = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=100)
    features = models.JSONField(default=list)
    offer_type = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
@receiver([post_save, post_delete], sender=OfferDetail)
def update_offer_min_values(sender, instance, **kwargs):
    offer = instance.offer
    agg = offer.details.aggregate(
        min_price=Min('price'),
        min_delivery_time=Min('delivery_time_in_days')
    )
    offer.min_price = agg['min_price'] if agg['min_price'] is not None else 0.0
    offer.min_delivery_time = agg['min_delivery_time'] if agg['min_delivery_time'] is not None else 7
    offer.save(update_fields=['min_price', 'min_delivery_time'])