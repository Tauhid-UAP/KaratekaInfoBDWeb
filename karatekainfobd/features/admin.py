from django.contrib import admin
from .models import Athlete, Club, Team

# Register your models here.

admin.site.register(Athlete)
admin.site.register(Club)
admin.site.register(Team)