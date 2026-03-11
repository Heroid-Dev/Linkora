from django.contrib import admin
from posts.models import Post,Comment,Like
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display=('title','author')
    search_fields=('title',)
    list_filter=('author',)
    ordering=('-created_at',)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model=Comment
    list_display=('post','author','content')
    search_fields=('content',)
    list_filter=('author',)
    ordering=('-created_at',)



@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    model=Like
    list_display=('user','post')
    search_fields = ('user__username','post__title')
    list_filter=('user__username',)
    ordering=('-created_at',)
