from django.urls import path
from .views import ListOrderView, SingleOrderView

urlpatterns = [
    path('orders/', ListOrderView.as_view(), name='list-orders'),
    path('orders/<int:pk>/', SingleOrderView.as_view(), name='single-order'),
]


