from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание', default='', blank=True)
    description_long = HTMLField('Длинное описание', null=True, blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField('Изображение')
    number = models.IntegerField('Номер', default=0, blank=True)
    place = models.ForeignKey(
        Place,
        verbose_name='Место на карте',
        on_delete=models.CASCADE,
        related_name='imgs',
    )
    
    def __str__(self):
        return f'{self.number} {self.place.title}'
    
    class Meta:
        ordering = ['number']
