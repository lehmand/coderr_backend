from rest_framework import generics
from profile_app.models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



    