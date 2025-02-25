from rest_framework import serializers
from django.contrib.auth.models import User
from auth_app.models import UserProfile
from rest_framework.authtoken.models import Token

class RegistrationSerializer(serializers.ModelSerializer):
    
    repeated_password = serializers.CharField(write_only=True)
    type = serializers.ChoiceField(choices=User.PROFILE_TYPES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'type']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['repeated_password']:
            raise serializers.ValidationError({'password': ['Die Passwörter stimmen nicht überein.']})   
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email': ['Diese E-mail wird bereits verwendet.']})
        return data
    
    def create(self, validated_data):
        validated_data.pop('repeated_password')
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user