from django.contrib import admin
from .models import Place, PlaceImage

# Register your models here.


class ImgInline(admin.TabularInline):
    model = PlaceImage
    verbose_name_plural = 'Фотографии'


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
         ImgInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage)
