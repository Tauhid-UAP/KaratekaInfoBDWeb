from django.db import models

# Create your models here.

GENDER_CHOICES = {
    ('Male', 'Male'),
    ('Female', 'Female'),
}

MALE_INDIVIDUAL_KATA_CHOICES = {
    ('Male Individual Kata', 'Male Individual Kata'),
    ('None', 'None'),
}

FEMALE_INDIVIDUAL_KATA_CHOICES = {
    ('Female Individual Kata', 'Female Individual Kata'),
    ('None', 'None'),
}

MALE_TEAM_KATA_CHOICES = {
    ('Male Team Kata', 'Male Team Kata'),
    ('None', 'None'),
}

FEMALE_TEAM_KATA_CHOICES = {
    ('Female Team Kata', 'Female Team Kata'),
    ('None', 'None'),
}

MALE_INDIVIDUAL_KUMITE_CHOICES = {
    ('-50kg Male Kumite', '-50kg Male Kumite'),
    ('-55kg Male Kumite', '-55kg Male Kumite'),
    ('-60kg Male Kumite', '-60kg Male Kumite'),
    ('-67kg Male Kumite', '-67kg Male Kumite'),
    ('-75kg Male Kumite', '-75kg Male Kumite'),
    ('-84kg Male Kumite', '-84kg Male Kumite'),
    ('+84kg Male Kumite', '+84kg Male Kumite'),
    ('None', 'None'),
}

FEMALE_INDIVIDUAL_KUMITE_CHOICES = {
    ('-45kg Female Kumite', '-45kg Female Kumite'),
    ('-50kg Female Kumite', '-50kg Female Kumite'),
    ('-55kg Female Kumite', '-55kg Female Kumite'),
    ('-61kg Female Kumite', '-61kg Female Kumite'),
    ('-68kg Female Kumite', '-68kg Female Kumite'),
    ('+68kg Female Kumite', '+68kg Female Kumite'),
    ('None', 'None')
}

MALE_INDIVIDUAL_KUMITE_CHOICES = {
    ('Male Team Kumite', 'Male Team Kumite'),
    ('None', 'None'),
}

FEMALE_INDIVIDUAL_KUMITE_CHOICES = {
    ('Female Team Kumite', 'Female Team Kumite'),
    ('None', 'None'),
}

class Athlete(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    feet_height = models.PositiveIntegerField(default=0)
    inch_height = models.PositiveIntegerField(default=0)
    weight = models.FloatField(default=0.0, help_text='Weight in kg')
    club = models.CharField(max_length=100, choices={
        ('Arrianna Academy' , 'Arrianna Academy'),
        ('Bangladesh Shitoryu Karate-do Union' , 'Bangladesh Shitoryu Karate-do Union')
    })
    team = models.CharField(max_length=100, choices={
        ('Bangladesh Ansar & VDP' , 'Bangladesh Ansar & VDP'),
        ('Bangladesh Army' , 'Bangladesh Army')
    })
    individual_kata_event = models.CharField(max_length=22, choices=[('', ''), ], default='None')
    individual_kumite_event = models.CharField(max_length=22, choices=[('', ''), ], default='None')
    team_kata_event = models.CharField(max_length=22, choices=[('', ''), ], default='None')
    team_kumite_event = models.CharField(max_length=22, choices=[('', ''), ], default='None')
    gold = models.PositiveIntegerField(default=0)
    silver = models.PositiveIntegerField(default=0)
    bronze = models.PositiveIntegerField(default=0)
    picture = models.ImageField(upload_to='athlete_images', blank=True)