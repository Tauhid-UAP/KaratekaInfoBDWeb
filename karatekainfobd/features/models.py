from django.db import models

from django.core.validators import MinValueValidator

from decimal import Decimal

from phone_field import PhoneField

# Create your models here.

# gender choices for gender field of Athlete
GENDER_CHOICES = {
    ('Male', 'Male'),
    ('Female', 'Female'),
}

# category choices for category field of Athlete

CADET_MALE_KATA = 'Cadet Male Kata'
CADET_MALE_KUMITE_0 = '-52kg Cadet Male Kumite'
CADET_MALE_KUMITE_1 = '-57kg Cadet Male Kumite'
CADET_MALE_KUMITE_2 = '-63kg Cadet Male Kumite'
CADET_MALE_KUMITE_3 = '-70kg Cadet Male Kumite'
CADET_MALE_KUMITE_4 = '+70kg Cadet Male Kumite'

CADET_FEMALE_KATA = 'Cadet Female Kata'
CADET_FEMALE_KUMITE_0 = '-47kg Cadet Female Kumite'
CADET_FEMALE_KUMITE_1 = '-54kg Cadet Female Kumite'
CADET_FEMALE_KUMITE_2 = '+54kg Cadet Female Kumite'

JUNIOR_MALE_KATA = 'Junior Male Kata'
JUNIOR_MALE_KUMITE_0 = '-55kg Junior Male Kumite'
JUNIOR_MALE_KUMITE_1 = '-61kg Junior Male Kumite'
JUNIOR_MALE_KUMITE_2 = '-68kg Junior Male Kumite'
JUNIOR_MALE_KUMITE_3 = '-76kg Junior Male Kumite'
JUNIOR_MALE_KUMITE_4 = '+76kg Junior Male Kumite'

JUNIOR_FEMALE_KATA = 'Junior Female Kata'
JUNIOR_FEMALE_KUMITE_0 = '-48kg Junior Female Kumite'
JUNIOR_FEMALE_KUMITE_1 = '-53kg Junior Female Kumite'
JUNIOR_FEMALE_KUMITE_2 = '-59kg Junior Female Kumite'
JUNIOR_FEMALE_KUMITE_3 = '+59kg Junior Female Kumite'

U21_MALE_KATA = 'U21 Male Kata'
U21_MALE_KUMITE_0 = '-50kg U21 Male Kumite'
U21_MALE_KUMITE_1 = '-55kg U21 Male Kumite'
U21_MALE_KUMITE_2 = '-60kg U21 Male Kumite'
U21_MALE_KUMITE_3 = '-67kg U21 Male Kumite'
U21_MALE_KUMITE_4 = '-75kg U21 Male Kumite'
U21_MALE_KUMITE_5 = '-84kg U21 Male Kumite'
U21_MALE_KUMITE_6 = '+84kg U21 Male Kumite'

U21_FEMALE_KATA = 'U21 Female Kata'
U21_FEMALE_KUMITE_0 = '-45kg U21 Female Kumite'
U21_FEMALE_KUMITE_1 = '-50kg U21 Female Kumite'
U21_FEMALE_KUMITE_2 = '-55g U21 Female Kumite'
U21_FEMALE_KUMITE_3 = '-61kg U21 Female Kumite'
U21_FEMALE_KUMITE_4 = '-68kg U21 Female Kumite'
U21_FEMALE_KUMITE_5 = '+68kg U21 Female Kumite'

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

# constants for athletes who participate
# in both Senior and U21 categories
# aged from 18 to 21
# U21_SENIOR_MALE_KATA = 'U21 Male Kata and Male Individual Kata'
# U21_SENIOR_MALE_KUMITE_0 = '-50kg U21 Male Kumite and -50kg Male Individual Kumite'
# U21_SENIOR_MALE_KUMITE_1 = '-55kg U21 Male Kumite and -55kg Male Individual Kumite'
# U21_SENIOR_MALE_KUMITE_2 = '-60kg U21 Male Kumite and -60kg Male Individual Kumite'
# U21_SENIOR_MALE_KUMITE_3 = '-67kg U21 Male Kumite and -67kg Male Individual Kumite'
# U21_SENIOR_MALE_KUMITE_4 = '-75kg U21 Male Kumite and -75kg Male Individual Kumite'
# U21_SENIOR_MALE_KUMITE_5 = '-84kg U21 Male Kumite and -84kg Male Individual Kumite'
# U21_SENIOR_MALE_KUMITE_6 = '+84kg U21 Male Kumite and +84kg Male Individual Kumite'
#
# U21_SENIOR_FEMALE_KATA = 'U21 Male Kata and Male Individual Kata'
# U21_SENIOR_FEMALE_KUMITE_0 = '-45kg U21 Female Kumite and -45kg Female Individual Kumite'
# U21_SENIOR_FEMALE_KUMITE_1 = '-50kg U21 Female Kumite and -50kg Female Individual Kumite'
# U21_SENIOR_FEMALE_KUMITE_2 = '-55kg U21 Female Kumite and -55kg Female Individual Kumite'
# U21_SENIOR_FEMALE_KUMITE_3 = '-61kg U21 Female Kumite and -61kg Female Individual Kumite'
# U21_SENIOR_FEMALE_KUMITE_4 = '-68kg U21 Female Kumite and -68kg Female Individual Kumite'
# U21_SENIOR_FEMALE_KUMITE_5 = '+68kg U21 Female Kumite and +68kg Female Individual Kumite'

# constants for position field of ChampionshipStanding
# position constants
FIRST_POSITION = 1
SECOND_POSITION = 2
THIRD_POSITION = 3

# medal constants
GOLD = 'Gold'
SILVER = 'Silver'
BRONZE = 'Bronze'

# The following lists are to be passed to the HTML as JSON strings

CADET_MALE_KATA_STRINGS = [CADET_MALE_KATA]
CADET_FEMALE_KATA_STRINGS = [CADET_FEMALE_KATA]
JUNIOR_MALE_KATA_STRINGS = [JUNIOR_FEMALE_KATA]
JUNIOR_FEMALE_KATA_STRINGS = [JUNIOR_FEMALE_KATA]
U21_MALE_KATA_STRINGS = [U21_MALE_KATA]
U21_FEMALE_KATA_STRINGS = [U21_FEMALE_KATA]
MALE_INDIVIDUAL_KATA_STRINGS = [MALE_INDIVIDUAL_KATA]
FEMALE_INDIVIDUAL_KATA_STRINGS = [FEMALE_INDIVIDUAL_KATA]
MALE_TEAM_KATA_STRINGS = [MALE_TEAM_KATA]
FEMALE_TEAM_KATA_STRINGS = [FEMALE_TEAM_KATA]

CADET_MALE_KUMITE_STRINGS = [
    CADET_MALE_KUMITE_0,
    CADET_MALE_KUMITE_1,
    CADET_MALE_KUMITE_2,
    CADET_MALE_KUMITE_3,
    CADET_MALE_KUMITE_4,
]

CADET_FEMALE_KUMITE_STRINGS = [
    CADET_FEMALE_KUMITE_0,
    CADET_FEMALE_KUMITE_1,
    CADET_FEMALE_KUMITE_2,
]

JUNIOR_MALE_KUMITE_STRINGS = [
    JUNIOR_MALE_KUMITE_0,
    JUNIOR_MALE_KUMITE_1,
    JUNIOR_MALE_KUMITE_2,
    JUNIOR_MALE_KUMITE_3,
    JUNIOR_MALE_KUMITE_4,
]

JUNIOR_FEMALE_KUMITE_STRINGS = [
    JUNIOR_FEMALE_KUMITE_0,
    JUNIOR_FEMALE_KUMITE_1,
    JUNIOR_FEMALE_KUMITE_2,
    JUNIOR_FEMALE_KUMITE_3,
]

U21_MALE_KUMITE_STRINGS = [
    U21_MALE_KUMITE_0,
    U21_MALE_KUMITE_1,
    U21_MALE_KUMITE_2,
    U21_MALE_KUMITE_3,
    U21_MALE_KUMITE_4,
    U21_MALE_KUMITE_5,
    U21_MALE_KUMITE_6,
]

U21_FEMALE_KUMITE_STRINGS = [
    U21_FEMALE_KUMITE_0,
    U21_FEMALE_KUMITE_1,
    U21_FEMALE_KUMITE_2,
    U21_FEMALE_KUMITE_3,
    U21_FEMALE_KUMITE_4,
    U21_FEMALE_KUMITE_5,
]

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

CADET_MALE_KATA_CHOICES = [
    (CADET_MALE_KATA, CADET_MALE_KATA),
]

CADET_FEMALE_KATA_CHOICES = [
    (CADET_FEMALE_KATA, CADET_FEMALE_KATA),
]

CADET_MALE_KUMITE_CHOICES = [
    (CADET_MALE_KUMITE_0, CADET_MALE_KUMITE_0),
    (CADET_MALE_KUMITE_1, CADET_MALE_KUMITE_1),
    (CADET_MALE_KUMITE_2, CADET_MALE_KUMITE_2),
    (CADET_MALE_KUMITE_3, CADET_MALE_KUMITE_3),
    (CADET_MALE_KUMITE_4, CADET_MALE_KUMITE_4),
]

CADET_FEMALE_KUMITE_CHOICES = [
    (CADET_FEMALE_KUMITE_0, CADET_FEMALE_KUMITE_0),
    (CADET_FEMALE_KUMITE_1, CADET_FEMALE_KUMITE_1),
    (CADET_FEMALE_KUMITE_2, CADET_FEMALE_KUMITE_2),
]

JUNIOR_MALE_KATA_CHOICES = [
    (JUNIOR_MALE_KATA, JUNIOR_MALE_KATA),
]

JUNIOR_FEMALE_KATA_CHOICES = [
    (JUNIOR_FEMALE_KATA, JUNIOR_FEMALE_KATA),
]

JUNIOR_MALE_KUMITE_CHOICES = [
    (JUNIOR_MALE_KUMITE_0, JUNIOR_MALE_KUMITE_0),
    (JUNIOR_MALE_KUMITE_1, JUNIOR_MALE_KUMITE_1),
    (JUNIOR_MALE_KUMITE_2, JUNIOR_MALE_KUMITE_2),
    (JUNIOR_MALE_KUMITE_3, JUNIOR_MALE_KUMITE_3),
    (JUNIOR_MALE_KUMITE_4, JUNIOR_MALE_KUMITE_4),
]

JUNIOR_FEMALE_KUMITE_CHOICES = [
    (JUNIOR_FEMALE_KUMITE_0, JUNIOR_FEMALE_KUMITE_0),
    (JUNIOR_FEMALE_KUMITE_1, JUNIOR_FEMALE_KUMITE_1),
    (JUNIOR_FEMALE_KUMITE_2, JUNIOR_FEMALE_KUMITE_2),
    (JUNIOR_FEMALE_KUMITE_3, JUNIOR_FEMALE_KUMITE_3),
]

U21_MALE_KATA_CHOICES = [
    (U21_MALE_KATA, U21_MALE_KATA),
]

U21_FEMALE_KATA_CHOICES = [
    (U21_FEMALE_KATA, U21_FEMALE_KATA),
]

U21_MALE_KUMITE_CHOICES = [
    (U21_MALE_KUMITE_0, U21_MALE_KUMITE_0),
    (U21_MALE_KUMITE_1, U21_MALE_KUMITE_1),
    (U21_MALE_KUMITE_2, U21_MALE_KUMITE_2),
    (U21_MALE_KUMITE_3, U21_MALE_KUMITE_3),
    (U21_MALE_KUMITE_4, U21_MALE_KUMITE_4),
    (U21_MALE_KUMITE_5, U21_MALE_KUMITE_5),
    (U21_MALE_KUMITE_6, U21_MALE_KUMITE_6),
]

U21_FEMALE_KUMITE_CHOICES = [
    (U21_FEMALE_KUMITE_0, U21_FEMALE_KUMITE_0),
    (U21_FEMALE_KUMITE_1, U21_FEMALE_KUMITE_1),
    (U21_FEMALE_KUMITE_2, U21_FEMALE_KUMITE_2),
    (U21_FEMALE_KUMITE_3, U21_FEMALE_KUMITE_3),
    (U21_FEMALE_KUMITE_4, U21_FEMALE_KUMITE_4),
    (U21_FEMALE_KUMITE_5, U21_FEMALE_KUMITE_5),
]

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

# position choices for ChampionshipStanding
POSITION_CHOICES = [
    (FIRST_POSITION, GOLD),
    (SECOND_POSITION, SILVER),
    (THIRD_POSITION, BRONZE),
]

# The following methods retrieve choices for the Athlete model

def get_all_u21_kata_choices():
    all_u21_kata_choices = []
    all_u21_kata_choices += U21_MALE_KATA_CHOICES
    all_u21_kata_choices += U21_FEMALE_KATA_CHOICES

    return all_u21_kata_choices

def get_all_u21_kumite_choices():
    all_u21_kumite_choices = []
    all_u21_kumite_choices += U21_MALE_KUMITE_CHOICES
    all_u21_kumite_choices += U21_MALE_KUMITE_CHOICES

    return all_u21_kumite_choices

def get_all_individual_kata_choices():
    all_individual_kata_choices = []
    all_individual_kata_choices += CADET_MALE_KATA_CHOICES
    all_individual_kata_choices += CADET_FEMALE_KATA_CHOICES
    all_individual_kata_choices += JUNIOR_MALE_KATA_CHOICES
    all_individual_kata_choices += JUNIOR_FEMALE_KATA_CHOICES
    # all_individual_kata_choices += U21_MALE_KATA_CHOICES
    # all_individual_kata_choices += U21_FEMALE_KATA_CHOICES
    all_individual_kata_choices+=MALE_INDIVIDUAL_KATA_CHOICES
    all_individual_kata_choices+=FEMALE_INDIVIDUAL_KATA_CHOICES

    return all_individual_kata_choices


def get_all_individual_kumite_choices():
    all_individual_kumite_choices = []
    all_individual_kumite_choices += CADET_MALE_KUMITE_CHOICES
    all_individual_kumite_choices += CADET_FEMALE_KUMITE_CHOICES
    all_individual_kumite_choices += JUNIOR_MALE_KUMITE_CHOICES
    all_individual_kumite_choices += JUNIOR_FEMALE_KUMITE_CHOICES
    # all_individual_kumite_choices += U21_MALE_KUMITE_CHOICES
    # all_individual_kumite_choices += U21_FEMALE_KUMITE_CHOICES
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

def get_all_category_choices():
    all_category_choices = []
    all_category_choices+=get_all_individual_kata_choices()
    all_category_choices += get_all_individual_kumite_choices()
    all_category_choices += get_all_team_kata_choices()
    all_category_choices += get_all_team_kumite_choices()

    return all_category_choices

# The following methods are to be used to retrieve the string constants
# To be converted to JSON strings

def get_all_cadet_male_kata_strings():
    return CADET_MALE_KATA_STRINGS

def get_all_cadet_female_kata_strings():
    return CADET_FEMALE_KATA_STRINGS

def get_all_cadet_male_kumite_strings():
    return CADET_MALE_KUMITE_STRINGS

def get_all_cadet_female_kumite_strings():
    return CADET_FEMALE_KUMITE_STRINGS

def get_all_junior_male_kata_strings():
    return JUNIOR_MALE_KATA_STRINGS

def get_all_junior_female_kata_strings():
    return JUNIOR_FEMALE_KATA_STRINGS

def get_all_junior_male_kumite_strings():
    return JUNIOR_MALE_KUMITE_STRINGS

def get_all_junior_female_kumite_strings():
    return JUNIOR_FEMALE_KUMITE_STRINGS

def get_all_u21_male_kata_strings():
    return U21_MALE_KATA_STRINGS

def get_all_u21_female_kata_strings():
    return U21_FEMALE_KATA_STRINGS

def get_all_u21_male_kumite_strings():
    return U21_MALE_KUMITE_STRINGS

def get_all_u21_female_kumite_strings():
    return U21_FEMALE_KUMITE_STRINGS

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

# method to get all choices
# of the position field of ChampionshipStanding
def get_all_position_choices():
    return POSITION_CHOICES

class Club(models.Model):
    name = models.CharField(max_length=50, unique=True)
    founded = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, default='')
    logo_picture = models.ImageField(upload_to='club_logos', blank=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone_number = PhoneField(blank=True, null=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    founded = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, default='')
    logo_picture = models.ImageField(upload_to='team_logos', blank=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone_number = PhoneField(blank=True, null=True)

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
    u21_kata_event = models.CharField(max_length=22, choices=get_all_u21_kata_choices(), blank=True, default="")
    u21_kata_active = models.BooleanField(default=False)
    u21_kumite_event = models.CharField(max_length=22, choices=get_all_u21_kumite_choices(), blank=True, default="")
    u21_kumite_active = models.BooleanField(default=False)
    gold = models.PositiveIntegerField(default=5)
    silver = models.PositiveIntegerField(default=5)
    bronze = models.PositiveIntegerField(default=5)
    description = models.CharField(max_length=100, blank=True, default='')
    picture = models.ImageField(upload_to='athlete_images', blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Championship(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    description = models.CharField(max_length=100)
    logo_picture = models.ImageField(upload_to='championship_logos', blank=True)

    def __str__(self):
        return self.title

class ChampionshipStanding(models.Model):
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    category = models.CharField(max_length=22, choices=get_all_category_choices(), default='')
    position = models.IntegerField(choices=get_all_position_choices())

    def __str__(self):
        return self.championship.__str__() + ' Position ' + str(self.position)