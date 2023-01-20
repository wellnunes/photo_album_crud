from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status

from photos.models import Photo
from photos.views import PhotoViewSet


class PhotoTest(TestCase):
    def setUp(self):
        self.photo = Photo.objects.create(
            name='Foto Teste',
            place='Local Teste',
            date='2023-01-20',
            photographer='Fotógrafo Teste',
            camera_flash=True,
        )
        self.factory = APIRequestFactory()
        self.viewset = PhotoViewSet
        self.data = {
            'name': 'Foto Teste',
            'place': 'Local Teste',
            'date': '2023-01-20',
            'photographer': 'Fotógrafo Teste',
            'camera_flash': True,
        }

    def test_get_photo_view_set(self):
        request = self.factory.get('')
        photo_detail = self.viewset.as_view({'get': 'retrieve'})
        response = photo_detail(request, pk=self.photo.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_photo_view_set(self):
        request = self.factory.get('')
        photo_list = self.viewset.as_view({'get': 'list'})
        response = photo_list(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
