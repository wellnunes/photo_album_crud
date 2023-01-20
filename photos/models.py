from django.db import models


class Photo(models.Model):
    name = models.CharField('Nome da foto', max_length=100)
    place = models.CharField('Local da foto', max_length=100)
    date = models.DateField('Data da foto')
    photographer = models.DateField('Local da foto', max_length=100)
    camera_flash = models.BooleanField('Flash da Câmera')

    # timestamps
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)
