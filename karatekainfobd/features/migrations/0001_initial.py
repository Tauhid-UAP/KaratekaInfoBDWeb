# Generated by Django 2.2 on 2020-04-13 15:52

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('founded', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('founded', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=100)),
                ('date_of_birth', models.DateField()),
                ('feet_height', models.PositiveIntegerField(default=0)),
                ('inch_height', models.DecimalField(decimal_places=1, default=0.0, max_digits=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('weight', models.FloatField(default=0.0, help_text='Weight in kg')),
                ('individual_kata_event', models.CharField(blank=True, choices=[('Male Individual Kata', 'Male Individual Kata'), ('Female Individual Kata', 'Female Individual Kata')], max_length=22, null=True)),
                ('individual_kumite_event', models.CharField(blank=True, choices=[('-50kg Male Kumite', '-50kg Male Kumite'), ('-55kg Male Kumite', '-55kg Male Kumite'), ('-60kg Male Kumite', '-60kg Male Kumite'), ('-67kg Male Kumite', '-67kg Male Kumite'), ('-75kg Male Kumite', '-75kg Male Kumite'), ('-84kg Male Kumite', '-84kg Male Kumite'), ('+84kg Male Kumite', '+84kg Male Kumite'), ('-45kg Female Kumite', '-45kg Female Kumite'), ('-50kg Female Kumite', '-50kg Female Kumite'), ('-55kg Female Kumite', '-55kg Female Kumite'), ('-61kg Female Kumite', '-61kg Female Kumite'), ('-68kg Female Kumite', '-68kg Female Kumite'), ('+68kg Female Kumite', '+68kg Female Kumite')], max_length=22, null=True)),
                ('team_kata_event', models.CharField(blank=True, choices=[('Male Team Kata', 'Male Team Kata'), ('Female Team Kata', 'Female Team Kata')], max_length=22, null=True)),
                ('team_kumite_event', models.CharField(blank=True, choices=[('Male Team Kumite', 'Male Team Kumite'), ('Female Team Kumite', 'Female Team Kumite')], max_length=22, null=True)),
                ('gold', models.PositiveIntegerField(default=5)),
                ('silver', models.PositiveIntegerField(default=5)),
                ('bronze', models.PositiveIntegerField(default=5)),
                ('picture', models.ImageField(blank=True, upload_to='athlete_images')),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='features.Club')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='features.Team')),
            ],
        ),
    ]
