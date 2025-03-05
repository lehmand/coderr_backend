from rest_framework import serializers
from orders_app.models import Order
from offers_app.models import OfferDetail
from django.contrib.auth.models import User
from profile_app.models import UserProfile


class OrderListSerializer(serializers.ModelSerializer):

    offer_detail_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'customer_user', 'business_user', 'title', 'revisions',
            'delivery_time_in_days', 'price', 'features', 'offer_type',
            'status', 'created_at', 'updated_at', 'offer_detail_id'
        ]
        read_only_fields = [
            'id', 'customer_user', 'business_user', 'title', 'revisions',
            'delivery_time_in_days', 'price', 'features', 'offer_type',
            'status', 'created_at', 'updated_at'
        ]

    def create(self, validated_data):
        offer_detail_id = validated_data.pop('offer_detail_id')
        offer_detail = OfferDetail.objects.get(id=offer_detail_id)
        offer = offer_detail.offer

        order = Order(
            customer_user = self.context['request'].user.id,
            business_user = offer.user.id,
            title = offer_detail.title,
            revisions = offer_detail.revisions,
            delivery_time_in_days = offer_detail.delivery_time_in_days,
            price = offer_detail.price,
            features = offer_detail.features,
            offer_type = offer_detail.offer_type,
            status = 'in_progress'
        )

        order.save()
        return order
    
    def validate_offer_detail_id(self, value):
        if not OfferDetail.objects.filter(id=value).exists():
            raise serializers.ValidationError('OfferDetail with this ID does not exist.')
        return value


