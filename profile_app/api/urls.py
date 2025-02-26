from django.urls import path
from .views import UserProfileDetailView, BusinessProfilesView, CustomerProfilesView

urlpatterns = [
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('profiles/business/', BusinessProfilesView.as_view(), name='business-profiles-list'),
    path('profiles/customer/', CustomerProfilesView.as_view(), name='customer-profiles-list'),
]
