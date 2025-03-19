from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import RegistrationSerializer
from rest_framework.permissions import AllowAny
from profile_app.models import UserProfile
from django.contrib.auth.models import User

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email,
                'user_id': user.id
            }, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class CustomAuthToken(ObtainAuthToken):
    permission_classes = [AllowAny]

    GUEST_USERS = {
            "andrey": {
                "password": "asdasd",
                "email": "customer@example.com",
                "type": "customer",
            },
            "kevin": {
                "password": "asdasd24",
                "email": "business@example.com",
                "type": "business",
            },
        }
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        serializer = self.get_serializer(data=request.data, context={'request': request})

        if self.is_guest_user(username, password):
            self.handle_guest_login(username, password)   

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email,
                'user_id': user.id
            }, status=HTTP_200_OK)
        return Response(serializer.erros, status=HTTP_400_BAD_REQUEST)
    
    def is_guest_user(self, username, password):
            return (
                username in self.GUEST_USERS
                and password == self.GUEST_USERS[username]["password"]
            )
    
    def handle_guest_login(self, username, password):
        user_data = self.GUEST_USERS[username]
        user, created = User.objects.get_or_create(
            username=username, defaults={"email": user_data["email"]}
        )
        if created:
            user.set_password(password)
            user.save()
            UserProfile.objects.create(user=user, type=user_data["type"])