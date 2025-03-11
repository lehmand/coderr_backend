from django_filters.rest_framework import FilterSet, NumberFilter
from offers_app.models import Offer

class OfferFilter(FilterSet):
    creator_id = NumberFilter(field_name='user', lookup_expr='exact')
    min_price = NumberFilter(field_name='min_price', lookup_expr='gte')
    max_delivery_time = NumberFilter(field_name='min_delivery_time', lookup_expr='lte')
    
    class Meta:
        model = Offer
        fields = ['creator_id', 'min_price', 'max_delivery_time']