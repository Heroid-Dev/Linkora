from django.urls import path
from notifications.api.v1 import views

urlpatterns = [
    path('',views.ListNotifications.as_view(),name='notification')
]
