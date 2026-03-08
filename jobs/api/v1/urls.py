from django.urls import path
from jobs.api.v1 import views

app_name='api-v1'

urlpatterns = [
    path('',views.JobsListView.as_view(),name='jobs-list'),
    path('<int:pk>/',views.JobsDetailView.as_view(),name='jobs-detail'),
    path('jobs/<int:job_id>/apply/',views.ApplyVeiw.as_view(),name='job_apply'),
    path('application/',views.ListAppView.as_view(),name='list-app'),
    path('application/<int:pk>/',views.RetrieveDestroyAppView.as_view(),name='detail-app')
]
