from django.db import models

from django.core.validators import MinValueValidator

from decimal import Decimal

# Create your models here.

GENDER_CHOICES = {
    ('Male', 'Male'),
    ('Female', 'Female'),
}

MALE_INDIVIDUAL_KATA = 'Male Individual Kata'
MALE_TEAM_KATA = 'Male Team Kata'
MALE_KUMITE_EVENT_0 = '-50kg Male Kumite'
MALE_KUMITE_EVENT_1 = '-55kg Male Kumite'
MALE_KUMITE_EVENT_2 = '-60kg Male Kumite'
MALE_KUMITE_EVENT_3 = '-67kg Male Kumite'
MALE_KUMITE_EVENT_4 = '-75kg Male Kumite'
MALE_KUMITE_EVENT_5 = '-84kg Male Kumite'
MALE_KUMITE_EVENT_6 = '+84kg Male Kumite'
MALE_TEAM_KUMITE = 'Male Team Kumite'

FEMALE_INDIVIDUAL_KATA = 'Female Individual Kata'
FEMALE_TEAM_KATA = 'Female Team Kata'
FEMALE_KUMITE_EVENT_0 = '-45kg Female Kumite'
FEMALE_KUMITE_EVENT_1 = '-50kg Female Kumite'
FEMALE_KUMITE_EVENT_2 = '-55kg Female Kumite'
FEMALE_KUMITE_EVENT_3 = '-61kg Female Kumite'
FEMALE_KUMITE_EVENT_4 = '-68kg Female Kumite'
FEMALE_KUMITE_EVENT_5 = '+68kg Female Kumite'
FEMALE_TEAM_KUMITE = 'Female Team Kumite'

# The following lists are to be passed to the HTML as JSON strings
MALE_INDIVIDUAL_KATA_STRINGS = [MALE_INDIVIDUAL_KATA]

FEMALE_INDIVIDUAL_KATA_STRINGS = [FEMALE_INDIVIDUAL_KATA]

MALE_TEAM_KATA_STRINGS = [MALE_TEAM_KATA]

FEMALE_TEAM_KATA_STRINGS = [FEMALE_TEAM_KATA]

MALE_INDIVIDUAL_KUMITE_STRINGS = [
    MALE_KUMITE_EVENT_0,
    MALE_KUMITE_EVENT_1,
    MALE_KUMITE_EVENT_2,
    MALE_KUMITE_EVENT_3,
    MALE_KUMITE_EVENT_4,
    MALE_KUMITE_EVENT_5,
    MALE_KUMITE_EVENT_6,
]

FEMALE_INDIVIDUAL_KUMITE_STRINGS = [
    FEMALE_KUMITE_EVENT_0,
    FEMALE_KUMITE_EVENT_1,
    FEMALE_KUMITE_EVENT_2,
    FEMALE_KUMITE_EVENT_3,
    FEMALE_KUMITE_EVENT_4,
    FEMALE_KUMITE_EVENT_5,
]

MALE_TEAM_KUMITE_STRINGS = [MALE_TEAM_KUMITE]

FEMALE_TEAM_KUMITE_STRINGS = [FEMALE_TEAM_KUMITE]

# The following lists are to be used
# As choices
MALE_INDIVIDUAL_KATA_CHOICES = [
    (MALE_INDIVIDUAL_KATA, MALE_INDIVIDUAL_KATA),
]
FEMALE_INDIVIDUAL_KATA_CHOICES = [
    (FEMALE_INDIVIDUAL_KATA, FEMALE_INDIVIDUAL_KATA),
]
MALE_TEAM_KATA_CHOICES = [
    (MALE_TEAM_KATA, MALE_TEAM_KATA),
]

FEMALE_TEAM_KATA_CHOICES = [
    (FEMALE_TEAM_KATA, FEMALE_TEAM_KATA),
]


MALE_INDIVIDUAL_KUMITE_CHOICES = [
    (MALE_KUMITE_EVENT_0, MALE_KUMITE_EVENT_0),
    (MALE_KUMITE_EVENT_1, MALE_KUMITE_EVENT_1),
    (MALE_KUMITE_EVENT_2, MALE_KUMITE_EVENT_2),
    (MALE_KUMITE_EVENT_3, MALE_KUMITE_EVENT_3),
    (MALE_KUMITE_EVENT_4, MALE_KUMITE_EVENT_4),
    (MALE_KUMITE_EVENT_5, MALE_KUMITE_EVENT_5),
    (MALE_KUMITE_EVENT_6, MALE_KUMITE_EVENT_6),
]

FEMALE_INDIVIDUAL_KUMITE_CHOICES = [
    (FEMALE_KUMITE_EVENT_0, FEMALE_KUMITE_EVENT_0),
    (FEMALE_KUMITE_EVENT_1, FEMALE_KUMITE_EVENT_1),
    (FEMALE_KUMITE_EVENT_2, FEMALE_KUMITE_EVENT_2),
    (FEMALE_KUMITE_EVENT_3, FEMALE_KUMITE_EVENT_3),
    (FEMALE_KUMITE_EVENT_4, FEMALE_KUMITE_EVENT_4),
    (FEMALE_KUMITE_EVENT_5, FEMALE_KUMITE_EVENT_5),
]

MALE_TEAM_KUMITE_CHOICES = [
    (MALE_TEAM_KUMITE, MALE_TEAM_KUMITE),
]

FEMALE_TEAM_KUMITE_CHOICES = [
    (FEMALE_TEAM_KUMITE, FEMALE_TEAM_KUMITE),
]

# The following methods retrieve choices for the Athlete model
def get_all_individual_kata_choices():
    all_individual_kata_choices = []
    all_individual_kata_choices+=MALE_INDIVIDUAL_KATA_CHOICES
    all_individual_kata_choices+=FEMALE_INDIVIDUAL_KATA_CHOICES

    return all_individual_kata_choices


def get_all_individual_kumite_choices():
    all_individual_kumite_choices = []
    all_individual_kumite_choices += MALE_INDIVIDUAL_KUMITE_CHOICES
    all_individual_kumite_choices += FEMALE_INDIVIDUAL_KUMITE_CHOICES

    return all_individual_kumite_choices


def get_all_team_kata_choices():
    all_team_kata_choices = []
    all_team_kata_choices += MALE_TEAM_KATA_CHOICES
    all_team_kata_choices += FEMALE_TEAM_KATA_CHOICES

    return all_team_kata_choices

def get_all_team_kumite_choices():
    all_team_kumite_choices = []
    all_team_kumite_choices += MALE_TEAM_KUMITE_CHOICES
    all_team_kumite_choices += FEMALE_TEAM_KUMITE_CHOICES

    return all_team_kumite_choices

# The following methods are to be used to retrieve the string constants
# To be converted to JSON strings
def get_all_male_individual_kata_strings():
    return MALE_INDIVIDUAL_KATA_STRINGS

def get_all_female_individual_kata_strings():
    return FEMALE_INDIVIDUAL_KATA_STRINGS

def get_all_male_team_kata_strings():
    return MALE_TEAM_KATA_STRINGS

def get_all_female_team_kata_strings():
    return FEMALE_TEAM_KATA_STRINGS

def get_all_male_individual_kumite_strings():
    return MALE_INDIVIDUAL_KUMITE_STRINGS

def get_all_female_individual_kumite_strings():
    return FEMALE_INDIVIDUAL_KUMITE_STRINGS

def get_all_male_team_kumite_strings():
    return MALE_TEAM_KUMITE_STRINGS

def get_all_female_team_kumite_strings():
    return FEMALE_TEAM_KUMITE_STRINGS

# Model to represent athletes

class Club(models.Model):
    name = models.CharField(max_length=50, unique=True)
    founded = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    founded = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Athlete(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    feet_height = models.PositiveIntegerField(default=0)
    inch_height = models.DecimalField(default=0.0, decimal_places=1, max_digits=3, validators=[MinValueValidator(Decimal(0.0))])
    weight = models.FloatField(default=0.0, help_text='Weight in kg')
    club = models.ForeignKey(Club, blank=True, null=True, on_delete=models.SET_NULL)
    team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.SET_NULL)
    individual_kata_event = models.CharField(max_length=22, choices=get_all_individual_kata_choices(), blank=True, default="")
    individual_kata_active = models.BooleanField(default=False)
    individual_kumite_event = models.CharField(max_length=22, choices=get_all_individual_kumite_choices(), blank=True, default="")
    individual_kumite_active = models.BooleanField(default=False)
    team_kata_event = models.CharField(max_length=22, choices=get_all_team_kata_choices(), blank=True, default="")
    team_kata_active = models.BooleanField(default=False)
    team_kumite_event = models.CharField(max_length=22, choices=get_all_team_kumite_choices(), blank=True, default="")
    team_kumite_active = models.BooleanField(default=False)
    gold = models.PositiveIntegerField(default=5)
    silver = models.PositiveIntegerField(default=5)
    bronze = models.PositiveIntegerField(default=5)
    picture = models.ImageField(upload_to='athlete_images', blank=True)