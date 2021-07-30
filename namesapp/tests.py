from django.test import TestCase
from .models import NYCAlready
# Create your tests here.
class NYCModelTests(TestCase):
    def setUp(self):
        NYCAlready.objects.create(name="FRANK, NODAL", book_and_case="13423445", location="AKMC")
        NYCAlready.objects.create(name="ABOGSE, KEVLIN", book_and_case="435467883", location="RIC")
    
    def test_all_entries_are_present(self):
        """
        returns True if there are 2 people in database
        """
        people = NYCAlready.objects.all()
        self.assertEqual(len(people), 2)
