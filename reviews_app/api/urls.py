from rest_framework.urls import path
from .views import ReviewListCreateView, ReviewSingleView

urlpatterns = [
    path('reviews/', ReviewListCreateView.as_view(), name='reviews'),
    path('reviews/<int:pk>/', ReviewSingleView.as_view(), name='single-review'),
]
