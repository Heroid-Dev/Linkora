from django.db import models


class Connection(models.Model):
    follower=models.ForeignKey('accounts.Profile',on_delete=models.CASCADE,related_name='following')
    following=models.ForeignKey('accounts.Profile',on_delete=models.CASCADE,related_name='folowers')
    
    established_date=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints= [ models.UniqueConstraint(fields=['following','follower'],name='unique_follow') ]
        
    def __str__(self):
        return f"{self.follower.user.username} is now following {self.following.user.username}"    