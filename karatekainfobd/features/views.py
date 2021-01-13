from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from django.views.generic import DetailView

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

from .utils import get_org_list_data, get_org_data, get_model_csv

from .filters import AthleteFilter

import json

from decouple import config

# Create your views here.

# def homepage(request):
#     context = {}
#     athlete_list = Athlete.objects.all().order_by('name')
#     athlete_filter = AthleteFilter(request.GET, queryset=athlete_list)
#     # context['athlete_list'] = athlete_list
#     context['athlete_filter'] = athlete_filter
#
#     paginated_athlete_filter = Paginator(athlete_filter.qs, 4)
#     page_number = request.GET.get('page')
#     athlete_page_obj = paginated_athlete_filter.get_page(page_number)
#
#     context['athlete_page_obj'] = athlete_page_obj
#
#     return render(request, 'features/homepage.html', context=context)

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

def start_date_comparator(e):
    return e.start_date

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

    # sort the championships list
    # by start_date
    # in reverse order
    championships.sort(reverse=True, key=start_date_comparator)

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

    championships = Championship.objects.all().order_by('-start_date')

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

# def show_all_clubs_page(request):
#     context = {}
#
#     clubs = Club.objects.all().order_by('name')
#
#     paginated_clubs = Paginator(clubs, 4)
#     page_number = request.GET.get('page')
#     club_page_obj = paginated_clubs.get_page(page_number)
#
#     context['club_page_obj'] = club_page_obj
#
#     return render(request, 'features/show_all_clubs_page.html', context=context)
#
#
# def show_all_teams_page(request):
#     context = {}
#
#     teams = Team.objects.all().order_by('name')
#
#     paginated_teams = Paginator(teams, 4)
#     page_number = request.GET.get('page')
#     team_page_obj = paginated_teams.get_page(page_number)
#
#     context['team_page_obj'] = team_page_obj
#
#     return render(request, 'features/show_all_teams_page.html', context=context)

def show_all_clubs_page(request):
    # pass Club to get data
    # corresponding to Club model
    context = get_org_list_data(request, Club)

    # pass the urlpattern name for club_detail
    context['org_detail_url_name'] = 'club_detail'

    for club in context['org_page_obj']:
        print(club.name)

    return render(request, 'features/show_all_orgs_page.html', context=context)


def show_all_teams_page(request):
    # pass Club to get data
    # corresponding to Club model
    context = get_org_list_data(request, Team)

    # pass the urlpattern name for team_detail
    context['org_detail_url_name'] = 'team_detail'

    return render(request, 'features/show_all_orgs_page.html', context=context)

# class ClubDetailView(DetailView):
#     model = Club
#     template_name = 'features/club_detail.html'
#
#     def get(self, request, pk) :
#         context = {}
#
#         club = Club.objects.get(id=pk)
#
#         try:
#             athletes = club.athlete_set.all().order_by('name')
#         except:
#             athletes = []
#
#         paginated_athletes = Paginator(athletes, 4)
#         page_number = request.GET.get('page')
#         athlete_page_obj = paginated_athletes.get_page(page_number)
#
#         context['club'] = club
#         context['athlete_page_obj'] = athlete_page_obj
#
#         return render(request, self.template_name, context)
#
# class TeamDetailView(DetailView):
#     model = Team
#     template_name = 'features/team_detail.html'
#
#     def get(self, request, pk) :
#         context = {}
#
#         team = Team.objects.get(id=pk)
#
#         try:
#             athletes = team.athlete_set.all().order_by('name')
#         except:
#             athletes = []
#
#         paginated_athletes = Paginator(athletes, 4)
#         page_number = request.GET.get('page')
#         athlete_page_obj = paginated_athletes.get_page(page_number)
#
#         context['team'] = team
#         context['athlete_page_obj'] = athlete_page_obj
#
#         return render(request, self.template_name, context)

class ClubDetailView(DetailView):
    model = Club
    template_name = 'features/org_detail.html'

    def get(self, request, pk) :
        context = get_org_data(request, self.model, pk)

        return render(request, self.template_name, context)

class TeamDetailView(DetailView):
    model = Team
    template_name = 'features/org_detail.html'

    def get(self, request, pk) :
        context = get_org_data(request, self.model, pk)

        return render(request, self.template_name, context)

# The following views are for staff only

# Extract model csvs'

# def get_athletes_csv(request, secret):
#     csv_secret = config('CSV_SECRET')
#
#     if secret == csv_secret:
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="athletes.csv"'
#         athletes = Athlete.objects.all()
#
#         writer = csv.writer(response)
#         writer.writerow([
#             'Name',
#             'Gender',
#             'Date of Birth',
#             'Feet',
#             'Inches',
#             'Weight',
#             'Club',
#             'Team',
#             'Ind. Kata',
#             'Active 1',
#             'Ind. Kumite',
#             'Active 2',
#             'Team Kata',
#             'Active 3',
#             'Team Kumite',
#             'Active 4',
#             'U21 Kata',
#             'Active 5',
#             'U21 Kumite',
#             'Active 6',
#             'Gold',
#             'Silver',
#             'Bronze',
#             'Description',
#             'Picture',
#             'Active'
#         ])
#
#         for athlete in athletes:
#             writer.writerow([
#                 athlete.name,
#                 athlete.gender,
#                 athlete.date_of_birth,
#                 athlete.feet_height,
#                 athlete.inch_height,
#                 athlete.weight,
#                 athlete.club,
#                 athlete.team,
#                 athlete.individual_kata_event,
#                 athlete.individual_kata_active,
#                 athlete.individual_kumite_event,
#                 athlete.individual_kumite_active,
#                 athlete.team_kata_event,
#                 athlete.team_kata_active,
#                 athlete.team_kumite_event,
#                 athlete.team_kumite_active,
#                 athlete.u21_kata_event,
#                 athlete.u21_kata_active,
#                 athlete.u21_kumite_event,
#                 athlete.u21_kumite_active,
#                 athlete.gold,
#                 athlete.silver,
#                 athlete.bronze,
#                 athlete.description,
#                 athlete.picture,
#                 athlete.active
#             ])
#
#         return response
#
#     else:
#         return redirect('homepage')

# def get_athletes_csv(request, secret):
#     csv_secret = config('CSV_SECRET')
#
#     if secret == csv_secret:
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="athletes.csv"'
#         athletes = Athlete.objects.all()
#
#         # get the tuple containing field names
#         fields_tuple = Athlete._meta.fields
#
#         # copy to list as tuples are immutable
#         fields = []
#         for field in fields_tuple:
#             fields.append(field)
#
#         fields.pop(0)
#
#         writer = csv.writer(response)
#         writer.writerow([field.name for field in fields])
#
#         for athlete in athletes:
#             writer.writerow([getattr(athlete, field.name) for field in fields])
#
#         return response
#
#     else:
#         return redirect('homepage')
#
# def get_clubs_csv(request, secret):
#     csv_secret = config('CSV_SECRET')
#     if secret == csv_secret:
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="clubs.csv"'
#         clubs = Club.objects.all()
#
#         writer = csv.writer(response)
#         writer.writerow([
#             'Name',
#             'Founded',
#             'Description',
#             'Logo'
#         ])
#
#         for club in clubs:
#             writer.writerow([
#                 club.name,
#                 club.founded,
#                 club.description,
#                 club.logo_picture
#             ])
#
#         return response
#
#     else:
#         return redirect('homepage')
#
# def get_teams_csv(request, secret):
#     csv_secret = config('CSV_SECRET')
#
#     if secret == csv_secret:
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="teams.csv"'
#         teams = Team.objects.all()
#
#         writer = csv.writer(response)
#         writer.writerow([
#             'Name',
#             'Founded',
#             'Description',
#             'Logo'
#         ])
#
#         for team in teams:
#             writer.writerow([
#                 team.name,
#                 team.founded,
#                 team.description,
#                 team.logo_picture
#             ])
#
#         return response
#
#     else:
#         return redirect('homepage')
#
# def get_championships_csv(request, secret):
#     csv_secret = config('CSV_SECRET')
#
#     if secret == csv_secret:
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="championships.csv"'
#         championships = Championship.objects.all()
#
#         writer = csv.writer(response)
#         writer.writerow([
#             'Title',
#             'Start Date',
#             'Description',
#             'Logo'
#         ])
#
#         for championship in championships:
#             writer.writerow([
#                 championship.title,
#                 championship.start_date,
#                 championship.description,
#                 championship.logo_picture
#             ])
#
#         return response
#
#     else:
#         return redirect('homepage')
#
# def get_championshipstandings_csv(request, secret):
#     csv_secret = config('CSV_SECRET')
#
#     if secret == csv_secret:
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="championshipstandings.csv"'
#         championshipstandings = ChampionshipStanding.objects.all()
#
#         writer = csv.writer(response)
#         writer.writerow([
#             'Championship',
#             'Athlete',
#             'Category',
#             'Position'
#         ])
#
#         for championshipstanding in championshipstandings:
#             writer.writerow([
#                 championshipstanding.championship,
#                 championshipstanding.athlete,
#                 championshipstanding.category,
#                 championshipstanding.position
#             ])
#
#         return response
#
#     else:
#         return redirect('homepage')


def get_athletes_csv(request, secret):
    return get_model_csv(request, Athlete, secret, 'athletes')

def get_clubs_csv(request, secret):
    return get_model_csv(request, Club, secret, 'clubs')

def get_teams_csv(request, secret):
    return get_model_csv(request, Team, secret, 'teams')

def get_championships_csv(request, secret):
    return get_model_csv(request, Championship, secret, 'championships')

def get_championshipstandings_csv(request, secret):
    return get_model_csv(request, ChampionshipStanding, secret, 'championshipstandings')