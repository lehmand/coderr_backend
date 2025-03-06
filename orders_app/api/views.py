from rest_framework import generics, status
from .serializers import ListOrderSerializer, SingleOrderSerializer
from orders_app.models import Order
from offers_app.models import OfferDetail
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Q

class ListOrderView(generics.ListCreateAPIView):
    serializer_class = ListOrderSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Order.objects.filter(Q(customer_user=user_id) | Q(business_user=user_id))
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class SingleOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = SingleOrderSerializer


    
        