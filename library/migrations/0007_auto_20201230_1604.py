# Generated by Django 3.1.3 on 2020-12-30 15:04

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20201230_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='books'),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100, verbose_name='Miejscowość'),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, verbose_name='Kraj'),
        ),
        migrations.AlterField(
            model_name='order',
            name='num_building',
            field=models.CharField(max_length=4, verbose_name='Numer mieszkania'),
        ),
        migrations.AlterField(
            model_name='order',
            name='post_code',
            field=models.CharField(max_length=6, verbose_name='Kod pocztowy'),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_name',
            field=models.CharField(max_length=100, verbose_name='Nazwa ulicy'),
        ),
    ]
