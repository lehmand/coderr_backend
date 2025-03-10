from rest_framework import generics
from profile_app.models import UserProfile
from .serializers import UserProfileSerializer, BusinessProfileSerializer, CustomerProfileSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
    
    def get_permissions(self):
        if self.request.method == 'PATCH':
            permission_classes = [IsAuthenticated, IsOwner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]



class BusinessProfilesView(generics.ListAPIView):
    queryset = UserProfile.objects.filter(type='business')
    serializer_class = BusinessProfileSerializer
    permission_classes = [IsAuthenticated]

class CustomerProfilesView(generics.ListAPIView):
    queryset = UserProfile.objects.filter(type='customer')
    serializer_class = CustomerProfileSerializer
    permission_classes = [IsAuthenticated]
    