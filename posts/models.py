from django.db import models

# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('accounts.Profile',on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    image=models.ImageField(upload_to='posts/',null=True,blank=True)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author=models.ForeignKey('accounts.Profile',on_delete=models.CASCADE,related_name='comments')
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return f"Comment by {self.author}"


class Like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='likes')
    user=models.ForeignKey('accounts.Profile',on_delete=models.CASCADE,related_name='liked_posts')
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('post','user')

    def __str__(self):
        return f"{self.user.user.username} liked {self.post.title}"


