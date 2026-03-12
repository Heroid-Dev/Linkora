from django.db import models
from django.utils.text import slugify


# Create your models here.

class Job(models.Model):
    employee=models.ForeignKey(
        'accounts.Profile',
        on_delete=models.CASCADE
    )
    
    title=models.CharField(max_length=255)
    description=models.TextField()
    location=models.CharField(max_length=255)
    is_remote=models.BooleanField(default=False)
    salary_min=models.IntegerField(null=True,blank=True)
    salary_max=models.IntegerField(null=True,blank=True)
    posted_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    category=models.ForeignKey('JobCategory',on_delete=models.CASCADE,related_name='jobs',null=True)
    skill=models.ManyToManyField('Skill',related_name='jobs',blank=True)
    
    class Meta:
        order_with_respect_to='employee'
    
    def __str__(self):
        return self.title
    
    
    
class Application(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name='applications')
    applicant=models.ForeignKey('accounts.Profile',on_delete=models.CASCADE,related_name='applications')
    
    resume=models.FileField()
    application_date=models.DateTimeField(auto_now_add=True)
    status= models.CharField(
        max_length=20,
        choices=[('Pending', 'در انتظار'), ('Reviewed', 'بررسی شده'), ('Accepted', 'پذیرفته شده'), ('Rejected', 'رد شده')],
        default='Pending'
    )
    
    class Meta:
        unique_together=('job','applicant')
        
    def __str__(self):
        return f'{self.applicant.user.email} for {self.job.title}'

class JobCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



    