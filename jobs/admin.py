from django.contrib import admin

from jobs.models import Job,Application
# Register your models here.


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=['employee','title','posted_date','is_active']
    list_filter=['is_remote', 'is_active', 'employee__user_type']
    search_fields=['title','description','location','employee__user_type']
    
    
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'status', 'application_date')
    list_filter = ('status', 'job__title', 'applicant__user_type')
    search_fields = ('job__title', 'applicant__user__email')
    