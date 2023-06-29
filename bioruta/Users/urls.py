from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from Users.views import RegisterView, RetriveUserView, RetrieveAdressView

urlpatterns = [
    path('address/', RetrieveAdressView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view()),
    path('me/', RetriveUserView.as_view())
    ]