from rest_framework import generics
from jobs.models import Application,Job
from ..serializer import ApplicationSerializer,JobSerializer,ApplicationStatusSerializer
from rest_framework import permissions
from ..permission import IsEmployer

    

class EmployerJobListCreateView(generics.ListCreateAPIView):
    serializer_class=JobSerializer
    permission_classes=[permissions.IsAuthenticated,IsEmployer]
    
    def get_queryset(self):
        return Job.objects.filter(employee=self.request.user.profile)
    
    def perform_create(self, serializer):
        serializer.save(employee=self.request.user.profile)


class EmployerApplicationListView(generics.ListAPIView):
    serializer_class=ApplicationSerializer
    permission_classes=[permissions.IsAuthenticated,IsEmployer]
    
    def get_queryset(self):
        return Application.objects.filter(job__employee=self.request.user.profile)
    
class EmployerApplicationUpdateView(generics.UpdateAPIView):
    serializer_class=ApplicationStatusSerializer
    permission_classes=[permissions.IsAuthenticated,IsEmployer]
    
    def get_queryset(self):
        return Application.objects.filter(job__employee=self.request.user.profile)
    
    
