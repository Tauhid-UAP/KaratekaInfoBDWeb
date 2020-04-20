from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Athlete
from .forms import AthleteForm

from .models import get_all_male_individual_kata_strings, get_all_female_individual_kata_strings, get_all_male_team_kata_strings, get_all_female_team_kata_strings, get_all_male_individual_kumite_strings, get_all_female_individual_kumite_strings, get_all_male_team_kumite_strings, get_all_female_team_kumite_strings

from .filters import AthleteFilter

import json

# Create your views here.

def homepage(request):
    return render(request, 'features/homepage.html')

def show_all_athletes_page(request):
    context = {}
    athlete_list = Athlete.objects.all()
    athlete_filter = AthleteFilter(request.GET, queryset=athlete_list)
    # context['athlete_list'] = athlete_list
    context['athlete_filter'] = athlete_filter

    paginated_athlete_filter = Paginator(athlete_filter.qs, 4)
    page_number = request.GET.get('page')
    athlete_page_obj = paginated_athlete_filter.get_page(page_number)

    context['athlete_page_obj'] = athlete_page_obj

    return render(request, 'features/show_all_athletes_page.html', context)

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
    male_individual_kumite_strings = get_all_male_individual_kumite_strings()
    female_individual_kumite_strings = get_all_female_individual_kumite_strings()
    male_team_kumite_strings = get_all_male_team_kumite_strings()
    female_team_kumite_strings = get_all_female_team_kumite_strings()

    json_male_individual_kata_strings = json.dumps(male_individual_kata_strings)
    json_female_individual_kata_strings = json.dumps(female_individual_kata_strings)
    json_male_team_kata_strings = json.dumps(male_team_kata_strings)
    json_female_team_kata_strings = json.dumps(female_team_kata_strings)
    json_male_individual_kumite_strings = json.dumps(male_individual_kumite_strings)
    json_female_individual_kumite_strings = json.dumps(female_individual_kumite_strings)
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
    context['male_individual_kumite_strings'] = json_male_individual_kumite_strings
    context['female_individual_kumite_strings'] = json_female_individual_kumite_strings
    context['male_team_kumite_strings'] = json_male_team_kumite_strings
    context['female_team_kumite_strings'] = json_female_team_kumite_strings

    return render(request, 'features/enter_athlete_page.html', context=context)