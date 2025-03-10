from rest_framework import generics
from .serializers import ReviewSerializer, ReviewSingleSerializer
from reviews_app.models import Review
from orders_app.api.permissions import IsCustomer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCreator

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

class ReviewSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSingleSerializer
    
    def get_permissions(self):
        
        if self.request.method in ['PATCH', 'DELETE']:
            permission_classes = [IsAuthenticated, IsCreator]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]