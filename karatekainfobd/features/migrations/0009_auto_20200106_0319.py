# Generated by Django 2.2 on 2020-01-05 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0008_auto_20200106_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=100),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='team',
            field=models.CharField(choices=[('AVDP', 'Bangladesh Ansar & VDP'), ('BA', 'Bangladesh Army')], max_length=100),
        ),
    ]