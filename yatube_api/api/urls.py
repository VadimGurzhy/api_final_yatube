from django.urls import include, path
from rest_framework import routers

from .views import (
    CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet,
    UserViewSet)

router_version_1 = routers.DefaultRouter()
router_version_1.register('posts', PostViewSet, basename='posts')
router_version_1.register('users', UserViewSet)
router_version_1.register(
    'posts/(?P<post_id>\\d+)/comments', CommentViewSet, basename='comments'
)
router_version_1.register('groups', GroupViewSet, basename='groups')
router_version_1.register('follow', FollowViewSet, basename='followers')

urlpatterns = [
    path('v1/', include(router_version_1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
