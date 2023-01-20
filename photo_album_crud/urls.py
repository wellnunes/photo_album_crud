from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from photos.views import PhotoViewSet
router = routers.DefaultRouter()
router.register('photos', PhotoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('openapi', get_schema_view(
                title="PhotoAlbum API",
                description="API para CRUD simples de um Album de Fotos",
                version="1.0.0"
            ), name='openapi-schema'),
    path('api/docs/', TemplateView.as_view(
            template_name='photos/swagger-ui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ), name='swagger-ui')
]
