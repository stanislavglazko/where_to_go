import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('links', nargs='+', type=str)

    def handle(self, *args, **options):
        for link in options['links']:
            place = requests.get(link)
            place.raise_for_status()
            place = place.json()
            new_place, created = Place.objects.get_or_create(
                title=place['title'],
                defaults={
                    'description_short': place['description_short'],
                    'description_long': place['description_long'],
                    'lng': place['coordinates']['lng'],
                    'lat': place['coordinates']['lat'],
                    'placeId': place['title'],
                },
            )

            for img_link in place['imgs']:
                response_img = requests.get(img_link)
                response_img.raise_for_status()
                content = ContentFile(response_img.content)
                new_img = PlaceImage(project=new_place)
                new_img.image.save(img_link, content, save=True)
