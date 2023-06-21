from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from PickUp.views import PickUpRequest
from django.contrib import admin


urlpatterns = [
   path('request', PickUpRequest.as_view(), name='create_pickUp'),
]
