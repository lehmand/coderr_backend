from rest_framework import serializers
from offers_app.models import Offer, OfferDetail
from django.contrib.auth.models import User
from profile_app.models import UserProfile

class OfferDetailNestedSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OfferDetail
        fields = ['id', 'url']
        extra_kwargs = {
            'url': {'view_name': 'offer-detail'}
        }

class OfferDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferDetail
        exclude = ['offer']
class OfferListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    details = OfferDetailNestedSerializer(many=True, read_only=True)
    min_price = serializers.FloatField(read_only=True)
    min_delivery_time = serializers.IntegerField(read_only=True)
    user_details = serializers.SerializerMethodField()
    class Meta:
        model = Offer
        fields = fields = [
            'id', 'user', 'title', 'image', 'description', 
            'created_at', 'updated_at', 'details',
            'min_price', 'min_delivery_time', 'user_details'
        ]

    def _update_min_values(self, offer, details_data):
        min_price = None
        min_delivery_time = None

        for detail_data in details_data:
            detail = OfferDetail.objects.create(offer=offer, **detail_data)
            min_price = min(min_price, detail.price) if min_price is not None else detail.price
            min_delivery_time = min(min_delivery_time, detail.delivery_time_in_days) if min_delivery_time is not None else detail.delivery_time_in_days

        offer.min_price = min_price if min_price is not None else 0.0
        offer.min_delivery_time = min_delivery_time if min_delivery_time is not None else 7
        offer.save(update_fields=['min_price', 'min_delivery_time'])

    
    def get_user_details(self, obj):
        user = obj.user
        return {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username
        }
    
class OfferCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(write_only=True, default=serializers.CurrentUserDefault())
    details = OfferDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Offer
        fields = ['id', 'user', 'title', 'image', 'description', 'details']

    def create(self, validated_data):
        details_data = self.initial_data.get('details', [])
        offer = Offer.objects.create(**validated_data)
        for detail in details_data:
            OfferDetail.objects.create(offer=offer, **detail)
        return offer
    
class SingleOfferSerializer(OfferCreateSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    details = OfferDetailNestedSerializer(many=True, read_only=True)
    min_price = serializers.SerializerMethodField()
    min_delivery_time = serializers.SerializerMethodField()
    
    class Meta:
        model = Offer
        fields = [
            'id', 'user', 'title', 'image', 'description',
            'created_at', 'updated_at', 'details',
            'min_price', 'min_delivery_time'
        ]

    def get_min_price(self, obj):
        details = obj.details.all()
        if details:
            return min(detail.price for detail in details)
        return None
    
    def get_min_delivery_time(self, obj):
        details = obj.details.all()
        if details:
            return min(detail.delivery_time_in_days for detail in details)
        return None
    
class UpdateSerializer(SingleOfferSerializer):
    user = None
    details = OfferDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Offer
        fields = ['id', 'title', 'image', 'description', 'details']