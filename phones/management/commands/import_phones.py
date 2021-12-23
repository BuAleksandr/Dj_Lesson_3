import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open("phones.csv") as f:
            phones = csv.DictReader(f, delimiter=';')
            for phone_info in phones:
                phone = Phone(id=phone_info.get('id'), name=phone_info.get('name'), price=int(phone_info.get('price')),
                              image=phone_info.get('image'), release_date=phone_info.get('release_date'),
                              lte_exists=bool(phone_info.get('lte_exists')), slug=phone_info.get('name'))
                phone.save()
