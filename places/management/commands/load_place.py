import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('links', nargs='+', type=str)

    def handle(self, *args, **options):
        for link in options['links']:
            place_raw = requests.get(link)
            place_raw.raise_for_status()
            place_raw = place_raw.json()
            place, created = Place.objects.get_or_create(
                title=place_raw['title'],
                defaults={
                    'description_short': place_raw['description_short'],
                    'description_long': place_raw['description_long'],
                    'lng': place_raw['coordinates']['lng'],
                    'lat': place_raw['coordinates']['lat'],
                },
            )

            for img_link in place_raw['imgs']:
                response_img = requests.get(img_link)
                response_img.raise_for_status()
                content = ContentFile(response_img.content)
                new_img = PlaceImage(place=place)
                new_img.image.save(img_link, content, save=True)
