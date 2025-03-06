from django.urls import path
from .views import ListOrderView, SingleOrderView, OrderCountView

urlpatterns = [
    path('orders/', ListOrderView.as_view(), name='list-orders'),
    path('orders/<int:pk>/', SingleOrderView.as_view(), name='single-order'),
    path('order-count/<int:business_user_id>/', OrderCountView.as_view(), name='order-count'),
]


