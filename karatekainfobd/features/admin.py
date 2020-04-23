from django.contrib import admin
from .models import Athlete, Club, Team, Championship, ChampionshipStanding

# Register your models here.

admin.site.register(Athlete)
admin.site.register(Club)
admin.site.register(Team)
admin.site.register(Championship)
admin.site.register(ChampionshipStanding)