from rest_framework import generics
from offers_app.models import Offer, OfferDetail
from .serializers import OfferCreateSerializer, OfferListSerializer, OfferDetailSerializer, SingleOfferSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class OfferListCreateView(generics.ListCreateAPIView):
    queryset = Offer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OfferListSerializer
        return OfferCreateSerializer

class SingleOfferView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = SingleOfferSerializer


class OfferDetailView(generics.RetrieveAPIView):
    queryset = OfferDetail.objects.all()
    serializer_class = OfferDetailSerializer