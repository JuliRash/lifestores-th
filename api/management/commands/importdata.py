from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

from api.models import Product
from api.product_data import products


class Command(BaseCommand):
    help = 'Imports products from a sample data'

    def handle(self, *args, **options):
        call_command('flush', '--no-input')

        for product in products:
            Product.objects.create(name=product['name'],
                                   description=product['description'],
                                   sku=product['sku'],
                                   price=product['price'],
                                   image=product['image'])


        self.stdout.write(self.style.SUCCESS('Successfully imported products data 🚀'))
