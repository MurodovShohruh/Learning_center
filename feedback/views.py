from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackViewSet(viewsets.ModelViewSet):

    queryset = Feedback.objects.all().order_by("created_at")
    serializer_class = FeedbackSerializer

    def get_permissions(self):

        if self.action in ["create"]:
            return [IsAuthenticatedOrReadOnly()]

        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsAdminUser()]

        return []