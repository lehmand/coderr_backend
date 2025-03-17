from rest_framework import serializers
from reviews_app.models import Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            'id',
            'business_user',
            'reviewer',
            'rating',
            'description',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'reviewer', 'created_at', 'updated_at']


    def create(self, validated_data):
        validated_data['reviewer'] = self.context['request'].user
        return super().create(validated_data)
    
    def validate(self, data):
        request = self.context.get('request')
        reviewer = request.user
        business_user = data.get('business_user')

        if Review.objects.filter(business_user=business_user, reviewer= reviewer).exists():
            raise serializers.ValidationError('Du hast bereits eine Bewertung abgegeben!')
        return data
    

class ReviewSingleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'business_user', 'reviewer', 'rating', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'business_user', 'reviewer', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
