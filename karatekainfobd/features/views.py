from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator

from .models import Athlete, Championship, ChampionshipStanding, Club, Team
from .forms import AthleteForm

from .models import get_all_male_individual_kata_strings,\
    get_all_female_individual_kata_strings,\
    get_all_male_team_kata_strings, get_all_female_team_kata_strings,\
    get_all_male_individual_kumite_strings,\
    get_all_female_individual_kumite_strings,\
    get_all_male_team_kumite_strings,\
    get_all_female_team_kumite_strings,\
    get_all_u21_male_kata_strings,\
    get_all_u21_female_kata_strings,\
    get_all_u21_male_kumite_strings,\
    get_all_u21_female_kumite_strings

from .filters import AthleteFilter

import json

# Create your views here.

def homepage(request):
    return render(request, 'features/homepage.html')

def show_all_athletes_page(request):
    context = {}
    athlete_list = Athlete.objects.all().order_by('name')
    athlete_filter = AthleteFilter(request.GET, queryset=athlete_list)
    # context['athlete_list'] = athlete_list
    context['athlete_filter'] = athlete_filter

    paginated_athlete_filter = Paginator(athlete_filter.qs, 4)
    page_number = request.GET.get('page')
    athlete_page_obj = paginated_athlete_filter.get_page(page_number)

    context['athlete_page_obj'] = athlete_page_obj

    return render(request, 'features/show_all_athletes_page.html', context=context)

def enter_athlete_page(request):
    context = {}


    if request.method == 'POST':
        athlete_form = AthleteForm(request.POST, request.FILES)

        if athlete_form.is_valid():
            athlete_form.save()
            return redirect('enter_athlete_page')

        context['athlete_form'] = athlete_form
    else:
        athlete_form = AthleteForm()
        context['athlete_form'] = athlete_form

    male_individual_kata_strings = get_all_male_individual_kata_strings()
    female_individual_kata_strings = get_all_female_individual_kata_strings()
    male_team_kata_strings = get_all_male_team_kata_strings()
    female_team_kata_strings = get_all_female_team_kata_strings()
    male_u21_kata_strings = get_all_u21_male_kata_strings()
    female_u21_kata_strings = get_all_u21_female_kata_strings()
    male_individual_kumite_strings = get_all_male_individual_kumite_strings()
    female_individual_kumite_strings = get_all_female_individual_kumite_strings()
    male_u21_kumite_strings = get_all_u21_male_kumite_strings()
    female_u21_kumite_strings = get_all_u21_female_kumite_strings()
    male_team_kumite_strings = get_all_male_team_kumite_strings()
    female_team_kumite_strings = get_all_female_team_kumite_strings()

    json_male_individual_kata_strings = json.dumps(male_individual_kata_strings)
    json_female_individual_kata_strings = json.dumps(female_individual_kata_strings)
    json_male_team_kata_strings = json.dumps(male_team_kata_strings)
    json_female_team_kata_strings = json.dumps(female_team_kata_strings)
    json_male_u21_kata_strings = json.dumps(male_u21_kata_strings)
    json_female_u21_kata_strings = json.dumps(female_u21_kata_strings)
    json_male_individual_kumite_strings = json.dumps(male_individual_kumite_strings)
    json_female_individual_kumite_strings = json.dumps(female_individual_kumite_strings)
    json_male_u21_kumite_strings = json.dumps(male_u21_kumite_strings)
    json_female_u21_kumite_strings = json.dumps(female_u21_kumite_strings)
    json_male_team_kumite_strings = json.dumps(male_team_kumite_strings)
    json_female_team_kumite_strings = json.dumps(female_team_kumite_strings)

    print(json_male_individual_kata_strings)
    print(json_female_individual_kata_strings)
    print(json_male_team_kata_strings)
    print(json_female_team_kata_strings)
    print(json_male_individual_kumite_strings)
    print(json_female_individual_kumite_strings)
    print(json_male_team_kumite_strings)
    print(json_female_team_kumite_strings)

    context['male_individual_kata_strings'] = json_male_individual_kata_strings
    context['female_individual_kata_strings'] = json_female_individual_kata_strings
    context['male_team_kata_strings'] = json_male_team_kata_strings
    context['female_team_kata_strings'] = json_female_team_kata_strings
    context['male_u21_kata_strings'] = json_male_u21_kata_strings
    context['female_u21_kata_strings'] = json_female_u21_kata_strings
    context['male_individual_kumite_strings'] = json_male_individual_kumite_strings
    context['female_individual_kumite_strings'] = json_female_individual_kumite_strings
    context['male_u21_kumite_strings'] = json_male_u21_kumite_strings
    context['female_u21_kumite_strings'] = json_female_u21_kumite_strings
    context['male_team_kumite_strings'] = json_male_team_kumite_strings
    context['female_team_kumite_strings'] = json_female_team_kumite_strings

    return render(request, 'features/enter_athlete_page.html', context=context)

def show_athlete_page(request, athlete_id):
    context = {}

    athlete = Athlete.objects.get(id=athlete_id)

    context['athlete'] = athlete

    return render(request, 'features/show_athlete_page.html', context=context)

def show_athlete_championships_page(request, athlete_id):
    context = {}

    athlete = Athlete.objects.get(id=athlete_id)
    championshipstandings = athlete.championshipstanding_set.all()

    # from championshipstandings
    # get all the championships
    # that the athlete
    # got medals in
    championships = []
    # dictionary to check
    # if current championship
    # has already been added
    already_added = {}
    for championshipstanding in championshipstandings:
        championship = championshipstanding.championship

        # statement will be false
        # if None
        if already_added.get(championship, None) is None:
            championships.append(championship)
            already_added[championship] = True

    context['athlete'] = athlete
    context['championships'] = championships

    return render(request, 'features/show_athlete_championships_page.html', context=context)

def show_athlete_championshipstandings_page(request, athlete_id, championship_id):
    context = {}

    athlete = Athlete.objects.get(id=athlete_id)
    championship = Championship.objects.get(id=championship_id)
    championshipstandings = ChampionshipStanding.objects.filter(athlete=athlete, championship=championship)

    context['athlete'] = athlete
    context['championship'] = championship
    context['championshipstandings'] = championshipstandings

    return render(request, 'features/show_athlete_championshipstandings_page.html', context=context)

def show_all_championships_page(request):
    context = {}

    championships = Championship.objects.all()

    paginated_championships = Paginator(championships, 4)
    page_number = request.GET.get('page')
    championship_page_obj = paginated_championships.get_page(page_number)

    context['championship_page_obj'] = championship_page_obj

    return render(request, 'features/show_all_championships_page.html', context=context)

def show_championshipstandings_page(request, championship_id):
    context = {}

    championship = Championship.objects.get(id=championship_id)
    championshipstandings = ChampionshipStanding.objects.filter(championship=championship)

    context['championship'] = championship
    context['championshipstandings'] = championshipstandings

    return render(request, 'features/show_championshipstandings_page.html', context=context)

def show_all_clubs_page(request):
    context = {}

    clubs = Club.objects.all().order_by('name')

    paginated_clubs = Paginator(clubs, 4)
    page_number = request.GET.get('page')
    club_page_obj = paginated_clubs.get_page(page_number)

    context['club_page_obj'] = club_page_obj

    return render(request, 'features/show_all_clubs_page.html', context=context)


def show_all_teams_page(request):
    context = {}

    teams = Team.objects.all().order_by('name')

    paginated_teams = Paginator(teams, 4)
    page_number = request.GET.get('page')
    team_page_obj = paginated_teams.get_page(page_number)

    context['team_page_obj'] = team_page_obj

    return render(request, 'features/show_all_teams_page.html', context=context)