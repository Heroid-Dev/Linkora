from django.urls import path
from connections.api.v1 import views


app_name='api-v1'


urlpatterns = [
    path('',views.ProfileListView.as_view(),name='profile-list'),
    path('<int:profile_id>/follow/',views.FollowUserView.as_view(),name='follow-view'),
    path('<int:pk>/unfollow/',views.UnfollowUserView.as_view(),name='unfollow-view'),
    path('following/',views.FollowingListView.as_view(),name='following_view'),
    path('follower/',views.FollowerListView.as_view(),name='follower-view'),
]
