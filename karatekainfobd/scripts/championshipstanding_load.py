import csv  # https://docs.python.org/3/library/csv.html

from decimal import Decimal

# https://django-extensions.readthedocs.io/en/latest/runscript.html

from features.models import ChampionshipStanding, Championship, Athlete

from features.utils import obj_or_none

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript athlete_load

# delete all athlete objects
# before repopulating database
ChampionshipStanding.objects.all().delete()

def run():

    # if file is not in the same directory as the scripts directory
    # then full path needs to be specified
    fhand = open('ChampionshipStandings.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    for row in reader:
        print(row)

        try:
            championship = Championship.objects.get(name=row[0])
        except:
            championship = obj_or_none(Championship, row[0])

        try:
            athlete = Athlete.objects.get(name=row[1])
        except:
            athlete = obj_or_none(Athlete, row[1])

        category = row[2]
        position = row[3]

        championshipstanding = ChampionshipStanding(
            athlete=athlete,
            championship=championship,
            category=category,
            position=position,
        )
        championshipstanding.save()
