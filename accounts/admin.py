from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUseAdmin
from accounts.models import Profile, User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','user_type']
    search_fields = ('user__email', 'user__username', 'headline', 'location')
    list_filter = ('user_type', 'is_premium')
    
    def get_readonly_fields(self, request, obj = None):
        if obj:
            return self.readonly_fields + ('user__email',)
        return self.readonly_fields
    


@admin.register(User)
class UserAdmin(BaseUseAdmin):
    list_display=['username','email','is_staff','is_superuser']
    list_filter=['is_staff','is_active']
    search_fields=['email','username']
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username','password1', 'password2', 'is_superuser', 'is_active','is_staff')}
        ),
        ('group permissions', 
         {
             'fields': ('groups','user_permissions',)
         }
        ),
        ('Important dates',
         {
             'fields': ('last_login',)
        }
         ),
    )
    
    
    fieldsets = (
        (None, {'fields': ('email','username', 'password')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
    def get_readonly_fields(self, request, obj = ...):
        if obj:
            return self.readonly_fields + ('email',)
        return super().get_readonly_fields(request, obj)
    
