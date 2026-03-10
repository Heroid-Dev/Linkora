from rest_framework import generics
from .serializer import ConnectionSerializer,ProfileListSerializer
from rest_framework import permissions
from accounts.models import Profile
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from connections.models import Connection

class FollowUserView(generics.CreateAPIView):
    queryset=Connection.objects.all()
    serializer_class=ConnectionSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    
    def perform_create(self, serializer):
        
        follower=self.request.user.profile
        following=get_object_or_404(Profile,id=self.kwargs['profile_id'])
        
        if follower == following :
            raise ValidationError('You cannot follow yourself')
        
        serializer.save(follower=follower,following=following)
        
class UnfollowUserView(generics.DestroyAPIView):
    queryset=Connection.objects.all()
    serializer_class=ConnectionSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def get_object(self):

        follower = self.request.user.profile
        following = get_object_or_404(Profile, id=self.kwargs["pk"])

        if follower == following:
            raise ValidationError("You cannot unfollow yourself")

        return get_object_or_404(
            Connection,
            follower=follower,
            following=following
        )
        
class FollowingListView(generics.ListAPIView):
    serializer_class=ConnectionSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Connection.objects.filter(follower=self.request.user.profile)
    
class FollowerListView(generics.ListAPIView):
    serializer_class=ConnectionSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Connection.objects.filter(following=self.request.user.profile)
    
class ProfileListView(generics.ListAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileListSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["request"] = self.request
    #     return context
    