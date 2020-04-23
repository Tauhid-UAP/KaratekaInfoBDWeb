# Generated by Django 2.2 on 2020-04-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0008_auto_20200420_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='club',
            name='logo_picture',
            field=models.ImageField(blank=True, upload_to='club_logos'),
        ),
        migrations.AddField(
            model_name='team',
            name='logo_picture',
            field=models.ImageField(blank=True, upload_to='team_logos'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100),
        ),
        migrations.AlterField(
            model_name='club',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]