from django.shortcuts import render
from django.http import HttpResponse
from .models import NYCAlready

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello and welcome to my first <u>Django App</u> project!</h1>")

