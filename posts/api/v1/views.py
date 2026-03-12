
from rest_framework.exceptions import ValidationError
from posts.models import Post,Comment,Like,PostCategory,Tag
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer,CommentSerializer,LikeSerializer,PostCategorySerializer,TagSerializer
from rest_framework import permissions, status
from notifications.models import Notification
from rest_framework.decorators import action
from rest_framework.response import Response
from connections.models import Connection
from django.db.models import Q,Count
from .paginations import PostPagination




class PostModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PostPagination

    queryset = Post.objects.select_related(
        "author", "author__user"
    )

    def get_serializer_class(self):
        if self.action in ['like','unlike','likes']:
            return LikeSerializer
        elif self.action in ['comment']:
            return CommentSerializer
        else:
            return PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)

    @action(detail=False, methods=['get'],permission_classes=[permissions.IsAuthenticated])
    def mine(self,request):
        posts= self.queryset.filter(author=self.request.user.profile)

        pages= self.paginate_queryset(posts)

        if pages is not None:
            serializer = self.get_serializer(pages,many=True)
            return self.get_paginated_response(serializer.data)

        serializer= self.get_serializer(posts,many=True)
        return Response(serializer.data)


    @action(detail=True, methods=['GET','POST'])
    def comment(self,request,pk):
        post= self.get_object()

        if request.method == 'GET':
            comments= Comment.objects.filter(post=post)
            serializer= self.get_serializer(comments,many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            serializer= self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(post=post,author=self.request.user.profile)
            Notification.objects.create(
                user=post.author.user,
                title='New Comment',
                message=f'New Comment for this post: {post.title}'
            )
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return None


    @action(detail=True,methods=['POST'])
    def like(self,request,pk=None):
        post= self.get_object()

        like,create=Like.objects.get_or_create(
            post=post,
            user=request.user.profile
        )

        if not create:
            return Response({"detail":"you already liked this post"},status=status.HTTP_400_BAD_REQUEST)

        Notification.objects.create(
            user=post.author.user,
            title='Like your post',
            message=f'user {request.user.username} liked your post {post.title}'
        )

        return Response({"detail":"Post liked."},status=status.HTTP_201_CREATED)


    @action(detail=True,methods=['POST'])
    def unlike(self,request,pk=None):
        post= self.get_object()
        like=Like.objects.filter(post=post,user=request.user.profile)
        if not like.exists():
            return Response({"detail":"You have not liked this post."},status=status.HTTP_400_BAD_REQUEST)
        like.delete()
        return Response({"detail":"Post unliked."},status=status.HTTP_204_NO_CONTENT)

    @action(detail=True,methods=['GET'])
    def likes(self,request,pk=None):
        post= self.get_object()
        likes=Like.objects.filter(post=post)
        serializer=self.get_serializer(likes,many=True)
        return Response(serializer.data)

    @action(detail=False,methods=['GET'])
    def feeds(self,request):
        followings = Connection.objects.filter(follower=request.user.profile).values_list('following', flat=True)
        posts = Post.objects.filter(Q(author__in=followings) | Q(author=request.user.profile))

        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


    @action(detail=False,methods=['GET'])
    def suggestions(self,request):
        following=Connection.objects.filter(follower=request.user.profile).values_list('following',flat=True)

        posts=Post.objects.exclude(Q(author__in=following) | Q(author=request.user.profile))[:20]

        pages=self.paginate_queryset(posts)
        if pages is not None:
            serializer= self.get_serializer(pages,many=True)
            return Response(serializer.data)

        serializer=self.get_serializer(posts,many=True)
        return Response(serializer.data)

    @action(detail=False,methods=['GET'])
    def trending(self,request):
        posts=Post.objects.annotate(
            like_count=Count('likes')
        ).order_by('-like_count')[:20]

        pages=self.paginate_queryset(posts)
        if pages is not None:
            serializer = self.get_serializer(pages,many=True)
            return Response(serializer.data)

        serializer=self.get_serializer(posts,many=True)
        return Response(serializer.data)


class PostCategoryModelViewSet(ModelViewSet):
    queryset = PostCategory.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostCategorySerializer

class TagModelViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TagSerializer








