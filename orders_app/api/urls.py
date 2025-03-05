from django.urls import path
from .views import OrderListView, OrderSingleView

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='list-orders'),
    path('orders/<int:pk>/', OrderSingleView.as_view(), name='single-order'),
]


