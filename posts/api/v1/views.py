from rest_framework.exceptions import ValidationError

from posts.models import Post,Comment
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer,CommentSerializer
from rest_framework import permissions, status
from rest_framework import generics
from notifications.models import Notification
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    queryset = Post.objects.select_related(
        "author", "author__user"
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)

    @action(detail=False, methods=['get'],permission_classes=[permissions.IsAuthenticated])
    def mine(self,request):
        posts= self.queryset.filter(author=self.request.user.profile)
        serializer= self.serializer_class(posts,many=True)
        return Response(serializer.data)


    @action(detail=True, methods=['GET','POST'])
    def comment(self,request,pk):
        post= self.get_object()

        if request.method == 'GET':
            comments= Comment.objects.filter(post=post)
            serializer= CommentSerializer(comments,many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            serializer= CommentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(post=post,author=self.request.user.profile)
            Notification.objects.create(
                user=post.author.user,
                title='New Comment',
                message=f'New Comment for this post: {post.title}'
            )
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return None


class CommentView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_post(self):
        return get_object_or_404(
            Post,
            id=self.kwargs['post_id']
        )

    def get_queryset(self):
        return Comment.objects.filter(post=self.get_post())

    def perform_create(self, serializer):
        post = self.get_post()

        Notification.objects.create(
            user=post.author.user,
            title='New Comment',
            message=f'New Comment for this post: {post.title}'
        )
        serializer.save(post=post,author=self.request.user.profile)


class AllPost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


