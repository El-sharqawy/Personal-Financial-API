from django.urls import path, include
from .views import CreateUserView, UserDetailView, UserBalanceView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('balance/', UserBalanceView.as_view(), name='user-balance'),
    path('register/', CreateUserView.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('api-auth/', include("rest_framework.urls")),
    ]
