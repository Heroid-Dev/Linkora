from rest_framework import generics
from jobs.models import Job
from ..serializer import JobSerializer
from rest_framework import permissions
from ..permission import IsEmployer



class JobsListView(generics.ListAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializer
    permission_classes=[permissions.IsAuthenticated]

        

class JobsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializer
    
    def get_permissions(self):
        if self.request.method in ["PUT","DELETE","PATCH"]:
            return [permissions.IsAuthenticated(),IsEmployer()]
        return [permissions.IsAuthenticated()]
    
    def perform_update(self, serializer):
        serializer.save(employee=self.request.user.profile)
    
    