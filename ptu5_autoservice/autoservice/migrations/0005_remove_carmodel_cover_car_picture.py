# Generated by Django 4.1.3 on 2022-11-16 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0004_carmodel_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='cover',
        ),
        migrations.AddField(
            model_name='car',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures', verbose_name='picture'),
        ),
    ]
