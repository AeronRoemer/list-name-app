from django.shortcuts import render
from .models import NYCAlready, NYCCurrent

# Create your views here.
def index(request):
    return render(request, 'namesapp/index.html')
    
def NYCRecentNames(request):
    people = NYCAlready.objects.all()
    context = { 'people': people }
    return render(request, 'namesapp/nyc-recent-names.html', context)
    