from rest_framework import serializers
from profile_app.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    first_name = serializers.CharField(source='user.first_name', default=None)
    last_name = serializers.CharField(source='user.last_name', default=None)
    file = serializers.ImageField(required=False, allow_null=True)
    created_at = serializers.DateTimeField(source='user.date_joined', read_only=True)
    class Meta:
        model = UserProfile
        fields = [
            'user',
            'username',
            'first_name',
            'last_name',
            'file',
            'location',
            'tel',
            'description',
            'working_hours',
            'type',
            'email',
            'created_at',
        ]

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user

        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        return super().update(instance, validated_data)


class BusinessProfileSerializer(UserProfileSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'username',
            'first_name',
            'last_name',
            'file',
            'location',
            'tel',
            'description',
            'working_hours',
            'type',
        ]

class CustomerProfileSerializer(UserProfileSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'username',
            'first_name',
            'last_name',
            'file',
            'type',
        ]