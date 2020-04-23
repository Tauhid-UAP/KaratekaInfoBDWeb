from django.urls import path
from . import views

# app_name='features'

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('show_all_athletes_page/', views.show_all_athletes_page, name='show_all_athletes_page'),
    path('enter_athlete_page/', views.enter_athlete_page, name='enter_athlete_page'),
    path('show_athlete_page/<int:athlete_id>/', views.show_athlete_page, name='show_athlete_page'),
    path('show_athlete_championships_page/<int:athlete_id>/', views.show_athlete_championships_page, name='show_athlete_championships_page'),
    path('show_athlete_championshipstandings_page/<int:athlete_id>/<int:championship_id>/', views.show_athlete_championshipstandings_page, name='show_athlete_championshipstandings_page'),
    path('show_all_championships_page/', views.show_all_championships_page, name='show_all_championships_page'),
    path('show_championshipstandings_page/<int:championship_id>/', views.show_championshipstandings_page, name='show_championshipstandings_page'),

]