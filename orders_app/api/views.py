from rest_framework import generics, status
from .serializers import OrderListSerializer
from orders_app.models import Order
from offers_app.models import OfferDetail
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    