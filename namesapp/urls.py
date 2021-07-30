from django.urls import path

from . import views

app_name = 'namesapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('nyc-all-names', views.NYCAllNames, name='nyc-all-names'),
    path('submit', views.submit, name='submit'),
]
