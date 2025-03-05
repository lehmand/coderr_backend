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
        offer_detail_id = request.data.get('offer_detail_id')

        if not offer_detail_id:
            return Response(
                {"error": "offer_detail_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        offer_detail = get_object_or_404(OfferDetail, id=offer_detail_id)
        offer = offer_detail.offer
        
        order_data = {
            'customer_user': request.user.id,
            'business_user': offer.user.id,
            'title': offer_detail.title,
            'revisions': offer_detail.revisions,
            'delivery_time_in_days': offer_detail.delivery_time_in_days,
            'price': offer_detail.price,
            'features': offer_detail.features,
            'offer_type': offer_detail.offer_type,
            'status': 'in_progress',
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        }

        order = Order.objects.create(**order_data)
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    