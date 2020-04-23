# Generated by Django 2.2 on 2020-04-13 16:02

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='inch_height',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
    ]