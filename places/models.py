from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    placeId = models.CharField('Идентификатор', max_length=200, default=None, blank=True)
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание', default='', blank=True)
    description_long = HTMLField('Длинное описание', null=True, blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField('Изображение', null=True, blank=True)
    number = models.IntegerField('Номер', default=0, blank=True)
    project = models.ForeignKey(
        Place,
        verbose_name='Проект',
        default=None,
        on_delete=models.CASCADE,
        related_name='imgs',
    )

    def __str__(self):
        return f'{self.number} {self.project.title}'
    
    class Meta:
        ordering = ['number']
