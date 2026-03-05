from ...models import Profile,User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import RegisterationSerializer,CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterationApiView(generics.GenericAPIView):
    serializer_class=RegisterationSerializer
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            email=serializer.validated_data['email']
            serializer.save()
            return Response({'email':email},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer