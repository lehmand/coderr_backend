from rest_framework import generics
from offers_app.models import Offer, OfferDetail
from .serializers import OfferSerializer, OfferDetailSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class OfferListView(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]

class OfferDetailView(generics.RetrieveAPIView):
    queryset = OfferDetail.objects.all()
    serializer_class = OfferDetailSerializer
    permission_classes = [AllowAny]