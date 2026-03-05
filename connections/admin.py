from django.contrib import admin
from connections.models import Connection
@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following', 'established_date')
    search_fields = ('follower__user__email', 'following__user__email')
    list_filter = ('established_date',)
