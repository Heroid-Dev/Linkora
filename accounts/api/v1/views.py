from ...models import Profile,User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .serializer import RegisterationSerializer,CustomTokenObtainPairSerializer,ChangePasswordSerializer,ProfileSerializer
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
    
class ChangePasswordView(generics.UpdateAPIView):
    model=User
    serializer_class=ChangePasswordSerializer
    permission_classes=[IsAuthenticated]
    
    def get_object(self):
        obj=self.request.user
        return obj
    
    def put(self, request, *args, **kwargs):
        self.object=self.get_object()
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not self.object.check_password(serializer.data.get('old_password')):
            return Response({"detail":"password wrong!"},status=status.HTTP_400_BAD_REQUEST)
        self.object.set_password(serializer.data.get('new_password'))
        self.object.save()
        return Response({"detail":"Change password successfully!"})
        
        


class ProfileRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated]
    
    def get_object(self):
        obj=get_object_or_404(self.get_queryset(),user=self.request.user)
        return obj
    
    