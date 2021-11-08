from django.db.models.fields.files import ImageFileDescriptor
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse

from .models import Place


def show_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_details = {
            "title": place.title,
            "imgs": [img.image.url for img in place.imgs.all()],
            "description_short": place.description_short,
            "description_long": place.description_long,
            "coordinates": {
                "lng": place.lng,
                "lat": place.lat,
            }
        }
    return JsonResponse(
        place_details,
        json_dumps_params={'ensure_ascii': False, 'indent': 4},
        )


def index(request):
    places = Place.objects.all()
    places_on_map = {
        "type": "FeatureCollection",
        "features": [],

    }
    for place in places:
        place_on_map = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "detailsUrl": reverse('places:place_view', args=[place.id])
            },
        }
        places_on_map['features'].append(place_on_map)

    return render(request, 'index.html', context={"places_on_map": places_on_map})
