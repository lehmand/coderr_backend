from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from .serializers import OfferCreateSerializer, OfferListSerializer, OfferDetailSerializer, SingleOfferSerializer
from .permissions import IsBusinessUser, IsCreator
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter
from offers_app.models import Offer, OfferDetail
from django.db.models import Min


class OfferListPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'

class OfferListCreateView(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['updated_at', 'min_price']
    search_fields = ['title', 'description']
    pagination_class = OfferListPagination

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
    serializer_class = SingleOfferSerializer

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