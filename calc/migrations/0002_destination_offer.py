# Generated by Django 3.0.2 on 2020-01-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='offer',
            field=models.BooleanField(default=False),
        ),
    ]
