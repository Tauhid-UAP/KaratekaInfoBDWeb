import csv  # https://docs.python.org/3/library/csv.html

from decimal import Decimal

# https://django-extensions.readthedocs.io/en/latest/runscript.html

from features.models import Championship

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript athlete_load

# delete all club objects
# before repopulating database
Championship.objects.all().delete()

def run():

    # if file is not in the same directory as the scripts directory
    # then full path needs to be specified
    fhand = open('Championships.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    for row in reader:
        print(row)

        name = row[0]
        start_date = row[1]

        if start_date == '':
            start_date = None

        description = row[2]
        logo_picture = row[3]

        championship = Championship(
            name=name,
            start_date=start_date,
            description=description,
            logo_picture=logo_picture,
        )
        championship.save()