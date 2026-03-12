from rest_framework.viewsets import ModelViewSet
from ..serializer import SkillSerializer
from rest_framework import permissions
from jobs.models import Skill

class SkillModelViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SkillSerializer