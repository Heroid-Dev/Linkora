from rest_framework import generics
from jobs.models import Job,Application
from .serializer import JobSerializer,ApplicationSerializer,JobApplySerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
class JobsListView(generics.GenericAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializer
    permission_classes=[permissions.IsAuthenticated,permissions.IsAuthenticatedOrReadOnly]
    
    
    def get(self,request):
        jobs=Job.objects.all()
        serializer=self.serializer_class(jobs,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(employee=request.user.profile)
        return Response(serializer.data,status=status.HTTP_201_CREATED)   
    

class JobsDetailView(generics.GenericAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializer
    permission_classes=[permissions.IsAuthenticated,permissions.IsAuthenticatedOrReadOnly]
    
    def get_object(self,pk,profile):
        try:
            return Job.objects.get(id=pk,employee=profile)
        except Job.DoesNotExist:
            return None
    
    def get(self,request,pk):
        job=self.get_object(pk,self.request.user.profile)
        if job:
            serializer= self.serializer_class(job)
            return Response(serializer.data)
        return Response({"detail":"this job not found!"})
    
    def put(self,request,pk):
        job=self.get_object(pk,self.request.user.profile)
        if job:
            serializer=self.serializer_class(job,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(employee=request.user.profile)
            return Response(serializer.data)
        return Response({"detail":"this job not found!"})
    
    def delete(self,request,pk):
        job=self.get_object(pk,self.request.user.profile)
        if job:
            return Response({"detail":f"delete {pk} job successfully!"})
        return Response({"detail":"this job not found!"})
        
        
class ApplyVeiw(generics.CreateAPIView):
    serializer_class=JobApplySerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def get_job(self):
        return get_object_or_404(Job,id=self.kwargs["job_id"])
    
    def get_serializer_context(self):
        context= super().get_serializer_context()
        context['job']=self.get_job()
        return context
    
    def perform_create(self, serializer):
        serializer.save(
            job=self.get_job(),
            applicant=self.request.user.profile
        )
        
class ListAppView(generics.ListAPIView):
    serializer_class=ApplicationSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user.profile)
    
class RetrieveDestroyAppView(generics.RetrieveDestroyAPIView):
    serializer_class=ApplicationSerializer
    permission_classes=[permissions.IsAuthenticated]

    
    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user.profile)
    