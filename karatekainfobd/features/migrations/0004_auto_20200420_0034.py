# Generated by Django 2.2 on 2020-04-19 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_auto_20200419_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100),
        ),
    ]