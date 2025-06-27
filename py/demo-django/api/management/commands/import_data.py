import csv
from django.core.management.base import BaseCommand
from api.models import ExampleCSVData


class Command(BaseCommand):
    help = 'Imports data from a CSV file into example CSV data model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            objects_to_create = []
            for row in reader:
                # Map CSV columns to model fields
                objects_to_create.append(ExampleCSVData(
                    col1=row['item1'],
                    col2=row['item2'],
                ))

            ExampleCSVData.objects.bulk_create(objects_to_create)
            self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
