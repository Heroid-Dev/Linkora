from rest_framework import serializers
from jobs.models import Job,Application



class JobSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(source='employee.user.email',read_only=True)
    salary_min = serializers.IntegerField(required=True)
    salary_max = serializers.IntegerField(required=True)

    class Meta:
        model=Job
        fields=['id','email','title','description','location','is_remote','salary_min','salary_max','posted_date','is_active']
        read_only_fields=['email']
        
    def validate_salary_min(self,value):
        if value < 0:    
            raise serializers.ValidationError("salary cannot be negative")
        return value
    
    def validate_salary_max(self,value):
        if value < 0:
            raise serializers.ValidationError("salary cannot be negative")
        return value
    
    def validate_title(self,value):
        if len(value) < 3:
            raise serializers.ValidationError("title is not short")
        return value
    
    def validate_description(self,value):
        if len(value) < 10:
            raise serializers.ValidationError("description is not short")
        return value
        
        
    def validate(self, attrs):
        salary_min=attrs.get('salary_min')
        salary_max=attrs.get('salary_max')
        if salary_min > salary_max and salary_max and salary_min:
            raise serializers.ValidationError("salary_min cannot be greater than salary_max")
        return super().validate(attrs)
        
    
class ApplicationSerializer(serializers.ModelSerializer):
    job_title=serializers.CharField(source='job.title')
    applicant_email=serializers.EmailField(source='applicant.user.email',read_only=True)
    class Meta:
        model=Application
        fields=[
                'id',
                'job',
                'job_title',
                'applicant_email',
                'resume',
                'status',
                'application_date'
                ]
        read_only_fields=['applicant_date','status']
        
class JobApplySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Application
        fields=['resume']
        
    def validate(self, attrs):
        request=self.context.get('request')
        job=self.context.get('job')
        
        if Application.objects.filter(job=job,applicant=request.user.profile).exists():
            raise serializers.ValidationError("you already applied for this job")
        
        # if job.employee == request.user.profile :
        #     raise serializers.ValidationError("You cannot apply to your own job.")
        return super().validate(attrs)
   

class ApplicationStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Application
        fields=['status']