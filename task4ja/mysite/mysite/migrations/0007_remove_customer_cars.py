# Generated by Django 4.0.1 on 2022-11-03 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_alter_customer_cars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='cars',
        ),
    ]
