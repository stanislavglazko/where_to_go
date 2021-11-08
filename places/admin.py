from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from .models import Place, PlaceImage


class ImgInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ('preview',)
    verbose_name_plural = 'Фотографии'
    extra = 0

    def preview(self, obj):
        return format_html('<img src="{}" height={} />', obj.image.url, 200)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    inlines = [
         ImgInline,
    ]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    raw_id_fields = ['place']
