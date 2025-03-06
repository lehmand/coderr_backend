from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .serializers import ListOrderSerializer, SingleOrderSerializer
from orders_app.models import Order
from offers_app.models import OfferDetail
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.views import APIView

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


class OrderCountView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request, business_user_id, *args, **kwargs):
        if not User.objects.filter(id=business_user_id).exists():
            return Response({"error": "Business user not found."}, status=status.HTTP_404_NOT_FOUND)
        
        order_count = Order.objects.filter(business_user=business_user_id, status='in_progress').count()
        return Response({"order_count": order_count}, status=status.HTTP_200_OK) 
    
    
