from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import NYCAlready, NYCCurrent

# Create your views here.
def index(request):
    return render(request, 'namesapp/index.html')
    
def NYCRecentNames(request):
    people = get_list_or_404(NYCAlready)
    context = { 'people': people }
    return render(request, 'namesapp/nyc-recent-names.html', context)

def submit(request):
    number = request.POST['number']
    context = { 'number': number }
    return render(request, 'namesapp/submit.html', context)
