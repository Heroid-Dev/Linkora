from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import Group

class UserManager(BaseUserManager):
    def create_user(self,email,username,password=None,**extra_fields):
        if not email:
            raise ValueError(_('the email must be set'))
        if not username:
            raise ValueError(_('the username must be set'))
        
        user=self.model(email=self.normalize_email(email),username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email,username,password,**extra_fields)
        

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True,max_length=255,null=False)
    username=models.CharField(max_length=255,unique=True,null=False)
    
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    
    objects=UserManager()
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=['username']
    
    
    
    def __str__(self):
        return self.email
    
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=255,unique=True)
    
    user_type=models.CharField(
        max_length=10,
        choices=[('INDIVIDUAL','Individual'),('COMPANY','Company')],
        default='INDIVIDUAL'
    )
    is_premium = models.BooleanField(default=False)
    
    headline = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    current_company = models.CharField(max_length=150, blank=True)
    
    def __str__(self):
        return f'{self.user.email} Profile'
    
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            Profile.objects.create(
                user=instance,
                username=instance.username,
                user_type="COMPANY"
            )
        else:
            Profile.objects.create(
                user=instance,
                username=instance.username
            )
    
    
    

