from django.shortcuts import redirect, HttpResponse

from .models import Athlete, Club, Team, Championship

from django.core.paginator import Paginator

from decouple import config

import csv

# show_all_clubs_page, show_all_teams_page, club_detail and team_detail views
# would have the same functionality
# so define util functions
# and pass the corresponding class type
# return the required data
def get_org_list_data(request, org_type):
    context = {}

    # org abstracts Club or Team objects
    org = org_type.objects.all().order_by('name')

    paginated_orgs = Paginator(org, 4)
    page_number = request.GET.get('page')
    org_page_obj = paginated_orgs.get_page(page_number)

    return {
        'org_page_obj' : org_page_obj,
    }

def get_org_data(request, org_type, pk):
    # org abstracts Club or Team object
    org = org_type.objects.get(id=pk)

    try:
        athletes = org.athlete_set.all().order_by('name')
    except:
        athletes = []

    paginated_athletes = Paginator(athletes, 4)
    page_number = request.GET.get('page')
    athlete_page_obj = paginated_athletes.get_page(page_number)

    return {
        'org': org,
        'athlete_page_obj': athlete_page_obj,
    }

# the following are for extracting model csvs'
def get_model_csv(request, model, secret, output_file):
    csv_secret = config('CSV_SECRET')

    if secret == csv_secret:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=' + model.__name__ + 's.csv'
        model_instances = model.objects.all()

        # get the tuple containing field names
        fields_tuple = model._meta.fields

        # copy to list as tuples are immutable
        fields = []
        for field in fields_tuple:
            fields.append(field)

        # remove the id field
        fields.pop(0)

        writer = csv.writer(response)
        writer.writerow([field.name for field in fields])

        for model_instance in model_instances:
            writer.writerow([getattr(model_instance, field.name) for field in fields])

        return response

    else:
        return redirect('homepage')

# the following functions
# for model_load scripts

def obj_or_none(org_type, name):
    if name:
        return obj_type.objects.create(name=name)

    return None