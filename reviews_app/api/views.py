from rest_framework import generics
from .serializers import ReviewSerializer, ReviewSingleSerializer
from reviews_app.models import Review

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSingleSerializer  