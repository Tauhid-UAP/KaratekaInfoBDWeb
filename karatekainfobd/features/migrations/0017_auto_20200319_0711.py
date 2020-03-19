# Generated by Django 2.2 on 2020-03-19 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0016_auto_20200318_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='club',
            field=models.CharField(choices=[('Arrianna Academy', 'Arrianna Academy'), ('Bangladesh Shitoryu Karate-do Union', 'Bangladesh Shitoryu Karate-do Union')], max_length=100),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=100),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='individual_kata_event',
            field=models.CharField(choices=[('None', 'None'), ('Male Individual Kata', 'Male Individual Kata'), ('Female Individual Kata', 'Female Individual Kata')], max_length=22),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='individual_kumite_event',
            field=models.CharField(choices=[('None', 'None'), ('-50kg Male Kumite', '-50kg Male Kumite'), ('-55kg Male Kumite', '-55kg Male Kumite'), ('-60kg Male Kumite', '-60kg Male Kumite'), ('-67kg Male Kumite', '-67kg Male Kumite'), ('-75kg Male Kumite', '-75kg Male Kumite'), ('-84kg Male Kumite', '-84kg Male Kumite'), ('+84kg Male Kumite', '+84kg Male Kumite'), ('-45kg Female Kumite', '-45kg Female Kumite'), ('-50kg Female Kumite', '-50kg Female Kumite'), ('-55kg Female Kumite', '-55kg Female Kumite'), ('-61kg Female Kumite', '-61kg Female Kumite'), ('-68kg Female Kumite', '-68kg Female Kumite'), ('+68kg Female Kumite', '+68kg Female Kumite')], max_length=22),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='team_kata_event',
            field=models.CharField(choices=[('None', 'None'), ('Male Team Kata', 'Male Team Kata'), ('Female Team Kata', 'Female Team Kata')], max_length=22),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='team_kumite_event',
            field=models.CharField(choices=[('None', 'None'), ('Male Team Kumite', 'Male Team Kumite'), ('Female Team Kumite', 'Female Team Kumite')], max_length=22),
        ),
    ]
