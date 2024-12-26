from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='user-list')
router.register(r'follows', FollowViewSet, basename='follow-list')
router.register(r'post', PostViewSet, basename='post-list')
router.register(r'post_like', PostLikeViewSet, basename='post_like-list')
router.register(r'comment', CommentViewSet, basename='comment-list')
router.register(r'comment_like', CommentLikeViewSet, basename='comment_like-list')
router.register(r'story', StoryViewSet, basename='story-list')
router.register(r'save', SaveViewSet, basename='save-list')
router.register(r'save_item', SaveItemViewSet, basename='save_item-list')


urlpatterns = [
    path('', include(router.urls))
]