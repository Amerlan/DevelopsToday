from django.urls import path, include
from rest_framework_nested import routers
from .views import PostViewSet, CommentViewSet

post_router = routers.SimpleRouter()
post_router.register('posts', PostViewSet)

comments_router = routers.NestedSimpleRouter(post_router, 'posts', lookup='post')
comments_router.register('comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('', include(post_router.urls)),
    path('', include(comments_router.urls)),
]
