from django.contrib import admin
from django.utils.html import format_html
from .models import Place, PlaceImage


class ImgInline(admin.TabularInline):
    model = PlaceImage
    readonly_fields = ('preview',)
    verbose_name_plural = 'Фотографии'

    def preview(self, obj):
        return format_html('<img src="{}" height={} />', obj.image.url, 200)


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
         ImgInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage)
