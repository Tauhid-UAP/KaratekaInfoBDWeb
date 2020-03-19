from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Athlete
from .forms import AthleteForm

# Create your views here.

def show_all_athletes_page(request):
    context = {}
    athlete_list = Athlete.objects.all()
    context['athlete_list'] = athlete_list

    paginated_athlete_list = Paginator(athlete_list, 4)
    page_number = request.GET.get('page')
    athlete_page_obj = paginated_athlete_list.get_page(page_number)

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

    return render(request, 'features/enter_athlete_page.html', context=context)