# Generated by Django 3.2.12 on 2022-02-13 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Buses', '0003_auto_20220212_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='start_date',
        ),
    ]
