from django.urls import path
from .views import OfferListCreateView, OfferDetailView, SingleOfferView

urlpatterns = [
    path('offers/', OfferListCreateView.as_view(), name='offer-list'),
    path('offers/<int:pk>/', SingleOfferView.as_view(), name='single-offer'),
    path('offerdetails/<int:pk>/', OfferDetailView.as_view(), name='offer-detail')
]
