from django.db import models


class Photo(models.Model):
    name = models.CharField('Nome da foto', max_length=100)
    place = models.CharField('Local da foto', max_length=100)
    date = models.DateField('Data da foto')
    photographer = models.DateField('Local da foto', max_length=100)
    camera_flash = models.BooleanField('Flash da Câmera')
