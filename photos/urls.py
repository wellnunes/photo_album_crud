from rest_framework import routers
from django.urls import path, include

from photos.views import PhotoViewSet

router = routers.DefaultRouter()
router.register('photos', PhotoViewSet)

app_name = 'photos'

urlpatterns = [
    path('', include(router.urls)),
]
