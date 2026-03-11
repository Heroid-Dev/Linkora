from django.urls import path
from rest_framework.routers import DefaultRouter
from posts.api.v1 import views
router=DefaultRouter()
router.register(r'',views.PostModelViewSet,basename='post')

urlpatterns = router.urls