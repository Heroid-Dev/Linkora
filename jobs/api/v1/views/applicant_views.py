from rest_framework import generics
from jobs.models import Job,Application
from ..serializer import ApplicationSerializer,JobApplySerializer
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from ..permission import IsApplicant
from notifications.models import Notification





class ApplyView(generics.CreateAPIView):
    serializer_class=JobApplySerializer
    permission_classes=[permissions.IsAuthenticated,IsApplicant]
    
    def get_job(self):
        return get_object_or_404(Job,id=self.kwargs["pk"])
    
    def get_serializer_context(self):
        context= super().get_serializer_context()
        context['job']=self.get_job()
        return context
    
    def perform_create(self, serializer):
        application=serializer.save(
            job=self.get_job(),
            applicant=self.request.user.profile
        )
        
        Notification.objects.create(
            user=self.get_job().employee.user,
            title=f'New Application from {self.request.user.username}',
            message=f'{self.request.user.email} applied for {application.job.title}'
        )
        
        
        

class ListAppView(generics.ListAPIView):
    serializer_class=ApplicationSerializer
    permission_classes=[permissions.IsAuthenticated,IsApplicant]
    
    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user.profile)
    
    
    
    
class RetrieveDestroyAppView(generics.RetrieveDestroyAPIView):
    serializer_class=ApplicationSerializer
    permission_classes=[permissions.IsAuthenticated,IsApplicant]

    
    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user.profile)