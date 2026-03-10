from rest_framework import generics
from .serializers import NotificationSerializer
from rest_framework import permissions
from notifications.models import Notification


class ListNotifications(generics.ListAPIView):
    serializer_class=NotificationSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
    