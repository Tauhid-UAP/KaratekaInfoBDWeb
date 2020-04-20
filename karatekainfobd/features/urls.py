from django.urls import path
from . import views

# app_name='features'

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('show_all_athletes_page/', views.show_all_athletes_page, name='show_all_athletes_page'),
    path('enter_athlete_page/', views.enter_athlete_page, name='enter_athlete_page'),

]