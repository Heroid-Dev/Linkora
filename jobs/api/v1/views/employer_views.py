from rest_framework import generics
from jobs.models import Application,Job
from ..serializer import ApplicationSerializer,JobSerializer,ApplicationStatusSerializer
from rest_framework import permissions
from ..permission import IsEmployer
from notifications.models import Notification

    

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
    
    def perform_update(self, serializer):
        application = serializer.save()
        
        if serializer.data.get('status') == 'Accepted':
            Notification.objects.create(
                user=application.applicant.user,
                title='Application Accepted',
                message=f'Your application for {application.job.title} has been accepted.'
            )
            
        if serializer.data.get('status') == 'Rejected':
            Notification.objects.create(
                user=application.applicant.user,
                title='Application Rejected',
                message=f'Your application for {application.job.title} was rejected.'
            )
    
    
