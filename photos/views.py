from rest_framework import viewsets, permissions, generics

from photos.models import Photo
from photos.serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Photo.objects.all()
        name = self.request.query_params.get('name')
        place = self.request.query_params.get('place')
        initial_date = self.request.query_params.get('initial_date')
        final_date = self.request.query_params.get('initial_date')
        photographer = self.request.query_params.get('photographer')
        camera_flash = self.request.query_params.get('camera_flash')

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if place is not None:
            queryset = queryset.filter(place__icontains=place)
        if initial_date and final_date:
            queryset = queryset.filter(date__range=(initial_date, final_date))
        if photographer is not None:
            queryset = queryset.filter(photographer__icontains=photographer)
        if camera_flash is not None:
            queryset = queryset.filter(camera_flash=camera_flash)

        return queryset
