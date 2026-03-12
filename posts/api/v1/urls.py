from django.urls import path
from rest_framework.routers import DefaultRouter
from posts.api.v1 import views
router=DefaultRouter()
router.register(r'post',views.PostModelViewSet,basename='post')
router.register(r'category',views.PostCategoryModelViewSet,basename='category')
router.register(r'tag',views.TagModelViewSet,basename='tag')

urlpatterns = router.urls