from django.db import models
import selenium

# Create your models here.
class NYCAlready(models.Model):
    name = models.CharField(max_length=250)
    book_and_case = models.CharField(max_length=40, primary_key=True)
    location = models.CharField(max_length=15)

    def __str__(self):
        return self.book_and_case

# Create your models here.
class NYCCurrent(models.Model):
    name = models.CharField(max_length=250)
    book_and_case = models.CharField(max_length=40)
    location = models.CharField(max_length=15)

    def __str__(self):
        return self.name, self.book_and_case, self.location