# Generated by Django 2.2 on 2020-05-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0019_athlete_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=100),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='individual_kata_event',
            field=models.CharField(blank=True, choices=[('Cadet Male Kata', 'Cadet Male Kata'), ('Cadet Female Kata', 'Cadet Female Kata'), ('Junior Male Kata', 'Junior Male Kata'), ('Junior Female Kata', 'Junior Female Kata'), ('U21 Male Kata', 'U21 Male Kata'), ('U21 Female Kata', 'U21 Female Kata'), ('Male Individual Kata', 'Male Individual Kata'), ('Female Individual Kata', 'Female Individual Kata')], default='', max_length=22),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='individual_kumite_event',
            field=models.CharField(blank=True, choices=[('-52kg Cadet Male Kumite', '-52kg Cadet Male Kumite'), ('-57kg Cadet Male Kumite', '-57kg Cadet Male Kumite'), ('-63kg Cadet Male Kumite', '-63kg Cadet Male Kumite'), ('-70kg Cadet Male Kumite', '-70kg Cadet Male Kumite'), ('+70kg Cadet Male Kumite', '+70kg Cadet Male Kumite'), ('-47kg Cadet Female Kumite', '-47kg Cadet Female Kumite'), ('-54kg Cadet Female Kumite', '-54kg Cadet Female Kumite'), ('+54kg Cadet Female Kumite', '+54kg Cadet Female Kumite'), ('-55kg Junior Male Kumite', '-55kg Junior Male Kumite'), ('-61kg Junior Male Kumite', '-61kg Junior Male Kumite'), ('-68kg Junior Male Kumite', '-68kg Junior Male Kumite'), ('-76kg Junior Male Kumite', '-76kg Junior Male Kumite'), ('+76kg Junior Male Kumite', '+76kg Junior Male Kumite'), ('-48kg Junior Female Kumite', '-48kg Junior Female Kumite'), ('-53kg Junior Female Kumite', '-53kg Junior Female Kumite'), ('-59kg Junior Female Kumite', '-59kg Junior Female Kumite'), ('+59kg Junior Female Kumite', '+59kg Junior Female Kumite'), ('-60kg U21 Male Kumite', '-60kg U21 Male Kumite'), ('-67kg U21 Male Kumite', '-67kg U21 Male Kumite'), ('-75kg U21 Male Kumite', '-75kg U21 Male Kumite'), ('-84kg U21 Male Kumite', '-84kg U21 Male Kumite'), ('+84kg U21 Male Kumite', '+84kg U21 Male Kumite'), ('-50kg U21 Female Kumite', '-50kg U21 Female Kumite'), ('-55g U21 Female Kumite', '-55g U21 Female Kumite'), ('-61kg U21 Female Kumite', '-61kg U21 Female Kumite'), ('-68kg U21 Female Kumite', '-68kg U21 Female Kumite'), ('+68kg U21 Female Kumite', '+68kg U21 Female Kumite'), ('-50kg Male Kumite', '-50kg Male Kumite'), ('-55kg Male Kumite', '-55kg Male Kumite'), ('-60kg Male Kumite', '-60kg Male Kumite'), ('-67kg Male Kumite', '-67kg Male Kumite'), ('-75kg Male Kumite', '-75kg Male Kumite'), ('-84kg Male Kumite', '-84kg Male Kumite'), ('+84kg Male Kumite', '+84kg Male Kumite'), ('-45kg Female Kumite', '-45kg Female Kumite'), ('-50kg Female Kumite', '-50kg Female Kumite'), ('-55kg Female Kumite', '-55kg Female Kumite'), ('-61kg Female Kumite', '-61kg Female Kumite'), ('-68kg Female Kumite', '-68kg Female Kumite'), ('+68kg Female Kumite', '+68kg Female Kumite')], default='', max_length=22),
        ),
        migrations.AlterField(
            model_name='championshipstanding',
            name='category',
            field=models.CharField(choices=[('Cadet Male Kata', 'Cadet Male Kata'), ('Cadet Female Kata', 'Cadet Female Kata'), ('Junior Male Kata', 'Junior Male Kata'), ('Junior Female Kata', 'Junior Female Kata'), ('U21 Male Kata', 'U21 Male Kata'), ('U21 Female Kata', 'U21 Female Kata'), ('Male Individual Kata', 'Male Individual Kata'), ('Female Individual Kata', 'Female Individual Kata'), ('-52kg Cadet Male Kumite', '-52kg Cadet Male Kumite'), ('-57kg Cadet Male Kumite', '-57kg Cadet Male Kumite'), ('-63kg Cadet Male Kumite', '-63kg Cadet Male Kumite'), ('-70kg Cadet Male Kumite', '-70kg Cadet Male Kumite'), ('+70kg Cadet Male Kumite', '+70kg Cadet Male Kumite'), ('-47kg Cadet Female Kumite', '-47kg Cadet Female Kumite'), ('-54kg Cadet Female Kumite', '-54kg Cadet Female Kumite'), ('+54kg Cadet Female Kumite', '+54kg Cadet Female Kumite'), ('-55kg Junior Male Kumite', '-55kg Junior Male Kumite'), ('-61kg Junior Male Kumite', '-61kg Junior Male Kumite'), ('-68kg Junior Male Kumite', '-68kg Junior Male Kumite'), ('-76kg Junior Male Kumite', '-76kg Junior Male Kumite'), ('+76kg Junior Male Kumite', '+76kg Junior Male Kumite'), ('-48kg Junior Female Kumite', '-48kg Junior Female Kumite'), ('-53kg Junior Female Kumite', '-53kg Junior Female Kumite'), ('-59kg Junior Female Kumite', '-59kg Junior Female Kumite'), ('+59kg Junior Female Kumite', '+59kg Junior Female Kumite'), ('-60kg U21 Male Kumite', '-60kg U21 Male Kumite'), ('-67kg U21 Male Kumite', '-67kg U21 Male Kumite'), ('-75kg U21 Male Kumite', '-75kg U21 Male Kumite'), ('-84kg U21 Male Kumite', '-84kg U21 Male Kumite'), ('+84kg U21 Male Kumite', '+84kg U21 Male Kumite'), ('-50kg U21 Female Kumite', '-50kg U21 Female Kumite'), ('-55g U21 Female Kumite', '-55g U21 Female Kumite'), ('-61kg U21 Female Kumite', '-61kg U21 Female Kumite'), ('-68kg U21 Female Kumite', '-68kg U21 Female Kumite'), ('+68kg U21 Female Kumite', '+68kg U21 Female Kumite'), ('-50kg Male Kumite', '-50kg Male Kumite'), ('-55kg Male Kumite', '-55kg Male Kumite'), ('-60kg Male Kumite', '-60kg Male Kumite'), ('-67kg Male Kumite', '-67kg Male Kumite'), ('-75kg Male Kumite', '-75kg Male Kumite'), ('-84kg Male Kumite', '-84kg Male Kumite'), ('+84kg Male Kumite', '+84kg Male Kumite'), ('-45kg Female Kumite', '-45kg Female Kumite'), ('-50kg Female Kumite', '-50kg Female Kumite'), ('-55kg Female Kumite', '-55kg Female Kumite'), ('-61kg Female Kumite', '-61kg Female Kumite'), ('-68kg Female Kumite', '-68kg Female Kumite'), ('+68kg Female Kumite', '+68kg Female Kumite'), ('Male Team Kata', 'Male Team Kata'), ('Female Team Kata', 'Female Team Kata'), ('Male Team Kumite', 'Male Team Kumite'), ('Female Team Kumite', 'Female Team Kumite')], default='', max_length=22),
        ),
    ]
