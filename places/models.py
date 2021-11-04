from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Длинное описание')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField('Изображение', null=True, blank=True)
    number = models.IntegerField('Номер')
    project = models.ForeignKey(
        Place,
        verbose_name='Проект',
        default=None,
        on_delete=models.CASCADE,
        related_name='Изображения',
    )

    def __str__(self):
        return f'{self.number} {self.project.title}' 
