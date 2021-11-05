from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'places'

urlpatterns = [
    path('', views.index, name='index'),
    path('places/<int:place_id>/', views.show_place, name='place_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
