from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer # type: ignore


# Create your views here.

class NotificationListView(generics.ListAPIView):
    """
    Fetch notifications for the authenticated user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)

class MarkNotificationAsReadView(generics.UpdateAPIView):
    """
    Mark a notification as read.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def patch(self, request, pk):
        notification = self.get_object()
        if notification.recipient != request.user:
            return Response({"error": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        notification.is_read = True
        notification.save()
        return Response({"success": "Notification marked as read."})
