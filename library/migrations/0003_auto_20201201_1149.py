# Generated by Django 3.1.3 on 2020-12-01 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20201201_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_end',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_start',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
