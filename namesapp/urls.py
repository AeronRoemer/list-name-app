from django.urls import path, include

from . import views

app_name = 'namesapp'
urlpatterns = [
    path('home', views.index, name='index'),
    path('ramNYC-all', views.NYCAllNames, name='ramNYC-all'),
    path('debug-driver', views.debug_driver, name='debug-driver'),
    path('get-names', views.get_names, name='get-names'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('return-csv-all', views.return_csv_all, name='return-csv-all'),
    path('return-csv-recent', views.return_csv_recent, name='return-csv-recent'),
    path('about', views.about, name='about'),
    path('most-recent-ramNYC', views.recent_NYC, name='most-recent-ramNYC'),
]
