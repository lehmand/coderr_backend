from rest_framework import generics
from profile_app.models import UserProfile
from .serializers import UserProfileSerializer, BusinessProfileSerializer, CustomerProfileSerializer

class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class BusinessProfilesView(generics.ListAPIView):
    queryset = UserProfile.objects.filter(type='business')
    serializer_class = BusinessProfileSerializer

class CustomerProfilesView(generics.ListAPIView):
    queryset = UserProfile.objects.filter(type='customer')
    serializer_class = CustomerProfileSerializer
    