from rest_framework import serializers
from orders_app.models import Order
from django.contrib.auth.models import User
from profile_app.models import UserProfile


class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            'id', 'customer_user', 'business_user', 'title', 'revisions',
            'delivery_time_in_days', 'price', 'features', 'offer_type',
            'status', 'created_at', 'updated_at'
        ]



