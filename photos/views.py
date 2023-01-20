from rest_framework import viewsets, permissions

from photos.models import Photo
from photos.serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """
    # Endpoint da API para visualizar, criar, editar ou deletar algum item.

    Podem ser consultadas todas as fotos, assim como a pesquisa/filtragem destas. **(Via Query Parameters)**

     - ?name=**NOME_DA_FOTO**  *(string)*

     - ?place=**LOCAL**  *(string)*

     - ?initial_date=**DATA_INICAL**&final_date=**DATA_FINAL**  *(ISO 8601)*

     - ?photographer=**NOME_DO_FOTÓGRAFO**  *(string)*
     
     - ?camera_flash=**TRUE_OR_FALSE**  *(boolean)*

    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Photo.objects.all()
        name = self.request.query_params.get('name')
        place = self.request.query_params.get('place')
        initial_date = self.request.query_params.get('initial_date')
        final_date = self.request.query_params.get('final_date')
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
