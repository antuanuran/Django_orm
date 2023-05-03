import csv
from datetime import datetime

from django.core.management import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phon in phones:
            slug = slugify(phon.get('name'))
            time_bad_format = phon["release_date"]
            time_result = datetime.strptime(time_bad_format, '%d.%m.%Y')

            Phone.objects.create(name=f'{phon["name"]}', price=f'{phon["price"]}', image=f'{phon["image"]}', release_date=f'{time_result}', lte_exists=f'{phon["lte_exists"]}', slug=slug)

