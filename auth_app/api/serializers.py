from rest_framework import serializers
from auth_app.models import User
from rest_framework.authtoken.models import Token

class RegistrationSerializer(serializers.ModelSerializer):
    
    repeated_password = serializers.CharField(write_only=True)
    type = serializers.ChoiceField(choices=User.PROFILE_TYPES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password', 'type']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['repeated_password']:
            raise serializers.ValidationError({'password': ['Die Passwörter stimmen nicht überein.']})
        return data
    
    def create(self, validated_data):
        validated_data.pop('repeated_password')
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user