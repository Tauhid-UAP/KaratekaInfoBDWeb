# Generated by Django 2.2 on 2020-04-20 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0013_auto_20200421_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100),
        ),
        migrations.AlterField(
            model_name='championshipstanding',
            name='position',
            field=models.IntegerField(choices=[(1, 'Gold'), (2, 'Silver'), (3, 'Bronze')]),
        ),
    ]