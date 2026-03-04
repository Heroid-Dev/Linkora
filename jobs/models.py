from django.db import models

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
    
    def __str__(self):
        return self.title
    
    
class Application(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    applicant=models.ForeignKey('accounts.Profile',on_delete=models.CASCADE)
    
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
        return f'{self.applicant.email} for {self.job.title}'
    