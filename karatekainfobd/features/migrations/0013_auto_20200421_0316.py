# Generated by Django 2.2 on 2020-04-20 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0012_championshipstanding_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=100),
        ),
        migrations.AlterField(
            model_name='championshipstanding',
            name='position',
            field=models.IntegerField(choices=[('Male Individual Kata', 'Male Individual Kata'), ('Female Individual Kata', 'Female Individual Kata'), ('-50kg Male Kumite', '-50kg Male Kumite'), ('-55kg Male Kumite', '-55kg Male Kumite'), ('-60kg Male Kumite', '-60kg Male Kumite'), ('-67kg Male Kumite', '-67kg Male Kumite'), ('-75kg Male Kumite', '-75kg Male Kumite'), ('-84kg Male Kumite', '-84kg Male Kumite'), ('+84kg Male Kumite', '+84kg Male Kumite'), ('-45kg Female Kumite', '-45kg Female Kumite'), ('-50kg Female Kumite', '-50kg Female Kumite'), ('-55kg Female Kumite', '-55kg Female Kumite'), ('-61kg Female Kumite', '-61kg Female Kumite'), ('-68kg Female Kumite', '-68kg Female Kumite'), ('+68kg Female Kumite', '+68kg Female Kumite'), ('Male Team Kata', 'Male Team Kata'), ('Female Team Kata', 'Female Team Kata'), ('Male Team Kumite', 'Male Team Kumite'), ('Female Team Kumite', 'Female Team Kumite')]),
        ),
    ]
