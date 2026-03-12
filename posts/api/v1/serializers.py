from rest_framework import serializers
from posts.models import Post,Comment,Like,PostCategory,Tag


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
    is_liked_by_user=serializers.SerializerMethodField(read_only=True)

    category = serializers.SlugRelatedField(slug_field='name', queryset=PostCategory.objects.all(), many=True)
    tag = serializers.SlugRelatedField(slug_field='name', queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Post
        fields=['id',
                'username',
                'title',
                'content',
                'image',
                'category',
                'tag',
                'created_at',
                'like_count',
                'is_liked_by_user',
                'comments_count',
                'comments']

    def get_is_liked_by_user(self,obj):
        return Like.objects.filter(post=obj,user=self.context['request'].user.profile).exists()

class LikeSerializer(serializers.ModelSerializer):
    username=serializers.ReadOnlyField(source='user.user.username')

    class Meta:
        model= Like
        fields=['post','username','created_at']
        read_only_fields=['post']


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= PostCategory
        fields=['id','name','slug']
        read_only_fields=['slug']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tag
        fields=['id','name','slug']
        read_only_fields=['slug']