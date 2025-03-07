from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .serializers import ListCreateOrderSerializer, SingleOrderSerializer
from .permissions import IsCustomer
from orders_app.models import Order
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.views import APIView
from offers_app.api.permissions import IsBusinessUser

class ListCreateOrderView(generics.ListCreateAPIView):
    serializer_class = ListCreateOrderSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Order.objects.filter(Q(customer_user=user_id) | Q(business_user=user_id))
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get_permissions(self):
        
        if self.request.method == 'POST':
            permission_classes = [IsAuthenticated, IsCustomer]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

class SingleOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = SingleOrderSerializer

    def get_permissions(self):
        
        if self.request.method in ['PATCH']:
            permission_classes = [IsAuthenticated, IsBusinessUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class OrderCountView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request, business_user_id, *args, **kwargs):
        if not User.objects.filter(id=business_user_id).exists():
            return Response({"error": "Business user not found."}, status=status.HTTP_404_NOT_FOUND)
        
        order_count = Order.objects.filter(business_user=business_user_id, status='in_progress').count()
        return Response({"order_count": order_count}, status=status.HTTP_200_OK) 
    
class CompleteOrderCountView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, business_user_id):
        if not User.objects.filter(id=business_user_id).exists():
            return Response({'error': 'Business user not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        complete_orders = Order.objects.filter(business_user=business_user_id, status='complete').count()
        return Response({'completed_order_count': complete_orders}, status=status.HTTP_200_OK)
