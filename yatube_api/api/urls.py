from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'v1/posts/', )

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
]
