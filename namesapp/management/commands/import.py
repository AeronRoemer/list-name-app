from namesapp.models import NYCAlready 
from csv import DictReader
from django.core.management import BaseCommand


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV file,
first destroy the database in PSQL.
Then, run `python manage.py migrate` for a new empty
database with tables"""

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from old-names.csv"

    def handle(self, *args, **options):
            
        # Show this before loading the data into the database
        print("Loading names data")


        #Code to load the data into database
        for row in DictReader(open('old-names-full-list.csv')):
            print(row)
            person=NYCAlready.objects.get_or_create(name=row['name'], book_and_case=row['booking_id'], location=row['current_facility'])  
            print(person)