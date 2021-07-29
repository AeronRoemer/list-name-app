from django.urls import path

from . import views

app_name = 'namesapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('nyc-recent-names', views.NYCRecentNames, name='nyc-recent-names'),
    path('submit', views.submit, name='submit'),
]
