from django.db import models
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('accounts.Profile',on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    image=models.ImageField(upload_to='posts/',null=True,blank=True)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category=models.ManyToManyField('PostCategory', related_name='posts',blank=True)
    tag=models.ManyToManyField('Tag',related_name='posts',blank=True)


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


class PostCategory(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(unique=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name







