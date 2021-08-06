from django.urls import path, include

from . import views

app_name = 'namesapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('ramNYC-all', views.NYCAllNames, name='ramNYC-all'),
    path('get-names', views.get_names, name='get-names'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
]
