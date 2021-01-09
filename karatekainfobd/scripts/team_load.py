import csv  # https://docs.python.org/3/library/csv.html

from decimal import Decimal

# https://django-extensions.readthedocs.io/en/latest/runscript.html

from features.models import Team

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript athlete_load

# delete all club objects
# before repopulating database
Team.objects.all().delete()

def run():

    # if file is not in the same directory as the scripts directory
    # then full path needs to be specified
    fhand = open('teams.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    for row in reader:
        print(row)

        name = row[0]
        founded = row[1]

        if founded == '':
            founded = None

        description = row[2]
        logo_picture = row[3]

        team = Team(
            name=name,
            founded=founded,
            description=description,
            logo_picture=logo_picture
        )
        team.save()