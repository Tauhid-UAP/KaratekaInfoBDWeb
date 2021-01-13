import django_filters

from .models import Athlete

class AthleteFilter(django_filters.FilterSet):
    weight__gte = django_filters.NumberFilter(field_name='weight', lookup_expr='gte')
    weight__lte = django_filters.NumberFilter(field_name='weight', lookup_expr='lte')

    class Meta:
        model = Athlete
        fields = [
            'name',
            'gender',
            'club',
            'team',
            'individual_kata_event',
            'individual_kata_active',
            'individual_kumite_event',
            'individual_kumite_active',
            'team_kata_event',
            'team_kata_active',
            'team_kumite_event',
            'team_kumite_active',
            'u21_kumite_event',
            'u21_kumite_active',
            'active',
        ]