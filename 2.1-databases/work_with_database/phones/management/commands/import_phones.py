import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify
from decimal import Decimal
from datetime import datetime


class Command(BaseCommand):
    help = 'Import phones from a CSV file into the Phone model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        try:
            with open(csv_file_path, 'r') as file:
                reader = csv.DictReader(file, delimiter=';')
                for row in reader:
                    try:
                        name = row['name']
                        price = Decimal(row['price'])
                        image = row['image']
                        release_date = datetime.strptime(row['release_date'], '%Y-%m-%d').date()
                        lte_exists = row['lte_exists'].lower() in ('true', '1', 'yes')

                        phone_obj, created = Phone.objects.get_or_create(
                            name=name,
                            defaults={
                                'price': price,
                                'image': image,
                                'release_date': release_date,
                                'lte_exists': lte_exists,
                                'slug': slugify(name),
                            }
                        )

                        if created:
                            self.stdout.write(self.style.SUCCESS(f'Successfully added phone: {name}'))
                        else:
                            self.stdout.write(self.style.WARNING(f'Phone {name} already exists'))

                    except ValueError as e:
                        self.stdout.write(self.style.ERROR(f'Error processing row: {row}. Error: {e}'))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Unexpected error: {e}'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {csv_file_path}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error opening file: {e}'))
