from django.shortcuts import render
from django.http import HttpResponse
from .models import NYCAlready, NYCCurrent

# Create your views here.
def index(request):
    people = NYCAlready.objects.all()
    output = ', '.join(p.name for p in people)
    return HttpResponse(output)