import django_filters

from .models import Athlete

class AthleteFilter(django_filters.FilterSet):

    class Meta:
        model = Athlete
        fields = [
            'name',
            'gender',
            'weight',
            'club',
            'team',
            'individual_kata_event',
            'individual_kumite_event',
            'team_kata_event',
            'team_kumite_event',
        ]