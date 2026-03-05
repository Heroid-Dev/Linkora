from django.urls import path
from accounts.api.v1 import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name='api-v1'

urlpatterns = [
    path('registeration/', views.RegisterationApiView.as_view(), name='registeration'),
    path('jwt/create/',views.CustomTokenObtainPairView.as_view(),name='jwt-create'),
    path('jwt/refresh/',TokenRefreshView.as_view(),name='jwt-refresh'),
    path('jwt/verify/',TokenVerifyView.as_view(),name='jwt-verify'),
]
