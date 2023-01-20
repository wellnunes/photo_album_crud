from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from photos.views import PhotoViewSet

router = routers.DefaultRouter()
router.register('photos', PhotoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
