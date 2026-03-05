from django.urls import path,include

app_name='jobs'

urlpatterns = [
    path('api/v1/',include('jobs.api.v1.urls')),
]
