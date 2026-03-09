from django.urls import path
from jobs.api.v1 import views

app_name='api-v1'

urlpatterns = [
    path('',views.JobsListView.as_view(),name='job-list'),
    path('<int:pk>/',views.JobsDetailView.as_view(),name='job-detail'),
    
    path('application/',views.ListAppView.as_view(),name='application-list'),
    path('application/<int:pk>/',views.RetrieveDestroyAppView.as_view(),name='application-detail'),
    path('<int:pk>/apply/',views.ApplyView.as_view(),name='job-apply'),
    
    path('employer/jobs/',views.EmployerJobListCreateView.as_view(),name='employer-jobs'),
    path('employer/applications/',views.EmployerApplicationListView.as_view(),name='employer-applications'),
    path('employer/applications/<int:pk>/status/',views.EmployerApplicationUpdateView.as_view(),name='employer-applications-status'),
    
    
    # کارفرما فقط Job های خودش را ببیند
    #کارجو فقط Application های خودش را ببیند
    #کارجو بتواند همه job ها را ببیند
    #کارفرما بتواند Application های job خودش را ببیند
]
