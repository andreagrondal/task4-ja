# Generated by Django 4.0.1 on 2022-11-03 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='booked_by',
        ),
        migrations.RemoveField(
            model_name='car',
            name='rented',
        ),
    ]
