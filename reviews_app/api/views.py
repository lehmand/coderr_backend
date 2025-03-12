from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from reviews_app.models import Review
from orders_app.api.permissions import IsCustomer
from .serializers import ReviewSerializer, ReviewSingleSerializer
from .permissions import IsCreator
from .filters import ReviewFilter

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsCustomer]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['updated_at', 'rating']
    filterset_class = ReviewFilter

class ReviewSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSingleSerializer
    
    def get_permissions(self):
        
        if self.request.method in ['PATCH', 'DELETE']:
            permission_classes = [IsAuthenticated, IsCreator]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]