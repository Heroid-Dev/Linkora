from django.contrib import admin

from jobs.models import Job,Application,JobCategory,Skill
# Register your models here.


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display=['employee','title','posted_date','is_active']
    list_filter=['is_remote', 'is_active', 'employee__user_type']
    search_fields=['title','description','location','employee__user_type']
    
    
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = ('job', 'applicant', 'status', 'application_date')
    list_filter = ('status', 'job__title', 'applicant__user_type')
    search_fields = ('job__title', 'applicant__user__email')


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    model = JobCategory
    list_display = ('name',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    model = Skill
    list_display = ('name',)