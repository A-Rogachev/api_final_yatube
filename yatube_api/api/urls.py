from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'v1/posts/', PostViewSet)
router.register(r'v1/groups/', GroupViewSet)
router.register(r'v1/comments/', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
