from rest_framework import generics
from offers_app.models import Offer, OfferDetail
from .serializers import OfferCreateSerializer, OfferListSerializer, OfferDetailSerializer, SingleOfferSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from .permissions import IsBusinessUser, IsCreator

class OfferListCreateView(generics.ListCreateAPIView):
    queryset = Offer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OfferListSerializer
        return OfferCreateSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [IsAuthenticated, IsBusinessUser]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]
    

class SingleOfferView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferCreateSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            permission_classes = [IsAuthenticated, IsCreator]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class OfferDetailView(generics.RetrieveAPIView):
    queryset = OfferDetail.objects.all()
    serializer_class = OfferDetailSerializer
    permission_classes = [AllowAny]