from rest_framework import serializers

from photos.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'name', 'place', 'date', 'photographer', 'camera_flash']
