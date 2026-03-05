from django.urls import path,include

app_name='connections'

urlpatterns = [
    path('api/v1/',include('connections.api.v1.urls')),
]
