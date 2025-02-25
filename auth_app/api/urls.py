from django.urls import path
from .views import RegistrationView, CustomAuthToken

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login')
]
