# Generated by Django 4.1.3 on 2022-11-16 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0007_remove_car_owner_order_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='owner',
        ),
    ]
