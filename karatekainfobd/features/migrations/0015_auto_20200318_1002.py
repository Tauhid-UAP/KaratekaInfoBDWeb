# Generated by Django 2.2 on 2020-03-18 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0014_auto_20200318_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='bronze',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='club',
            field=models.CharField(choices=[('Bangladesh Shitoryu Karate-do Union', 'Bangladesh Shitoryu Karate-do Union'), ('Arrianna Academy', 'Arrianna Academy')], max_length=100),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='feet_height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='gold',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='inch_height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='silver',
            field=models.PositiveIntegerField(default=0),
        ),
    ]