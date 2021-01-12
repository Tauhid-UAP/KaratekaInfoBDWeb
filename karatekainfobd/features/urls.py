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

    path('show_all_clubs_page/', views.show_all_clubs_page, name='show_all_clubs_page'),
    path('show_all_teams_page/', views.show_all_teams_page, name='show_all_teams_page'),

    path('club_detail/<int:pk>/', views.ClubDetailView.as_view(), name='club_detail'),
    path('team_detail/<int:pk>/', views.TeamDetailView.as_view(), name='team_detail'),


    path('get_athletes_csv/<slug:secret>/', views.get_athletes_csv, name='get_athletes_csv'),
    path('get_clubs_csv/<slug:secret>/', views.get_clubs_csv, name='get_clubs_csv'),
    path('get_teams_csv/<slug:secret>/', views.get_teams_csv, name='get_teams_csv'),
    path('get_championships_csv/<slug:secret>/', views.get_championships_csv, name='get_championships_csv'),
    path('get_championshipstandings_csv/<slug:secret>/', views.get_championshipstandings_csv, name='get_championshipstandings_csv')
]