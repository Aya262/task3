# Generated by Django 3.2.12 on 2022-02-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busroute',
            name='station_list',
        ),
        migrations.AddField(
            model_name='busroute',
            name='station_list',
            field=models.ManyToManyField(to='Buses.Station'),
        ),
    ]
