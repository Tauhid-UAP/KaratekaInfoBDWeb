# Generated by Django 2.2 on 2020-01-05 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0010_auto_20200106_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='club',
            field=models.CharField(choices=[('BSKU', 'Bangladesh Shitoryu Karate-do Union'), ('SKAA', 'Arrianna Academy')], max_length=100),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
