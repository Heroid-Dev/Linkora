from rest_framework import serializers
from posts.models import Post,Comment,Like



class CommentSerializer(serializers.ModelSerializer):
    username=serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields=['username','content','created_at']



class PostSerializer(serializers.ModelSerializer):
    username=serializers.ReadOnlyField(source='author.user.username')
    comments=CommentSerializer(many=True,read_only=True)
    comments_count=serializers.IntegerField(source='comments.count',read_only=True)
    like_count=serializers.IntegerField(source='likes.count',read_only=True)

    class Meta:
        model = Post
        fields=['username','title','content','image','created_at','like_count','comments_count','comments']


class LikeSerializer(serializers.ModelSerializer):
    username=serializers.ReadOnlyField(source='user.user.username')

    class Meta:
        model= Like
        fields=['post','username','created_at']
        read_only_fields=['post']
