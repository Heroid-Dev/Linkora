from rest_framework.viewsets import ModelViewSet
from ..serializer import JobCategorySerializer
from rest_framework import permissions
from jobs.models import JobCategory

class JobCategoryModelViewSet(ModelViewSet):
    queryset = JobCategory.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = JobCategorySerializer