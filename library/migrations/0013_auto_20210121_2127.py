# Generated by Django 3.1.3 on 2021-01-21 20:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20210121_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Zły format miejscowości: tylko litery', regex='[a-zA-ZŻŹĆĄŚĘŃŁÓżźćąśęńłó]')], verbose_name='Miejscowość'),
        ),
        migrations.AlterField(
            model_name='order',
            name='num_building',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(message='Zły format numeru mieszkania: XXXX(cyfry)', regex='[0-9]')], verbose_name='Numer mieszkania'),
        ),
        migrations.AlterField(
            model_name='order',
            name='num_door',
            field=models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator(message='Zły format numeru lokalu: XXXX(cyfry)', regex='[0-9]')], verbose_name='Numer lokalu'),
        ),
        migrations.AlterField(
            model_name='order',
            name='post_code',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Zły format kodu pocztowego: XX-XXX (cyfry)', regex='\\d{2}-\\d{3}')], verbose_name='Kod pocztowy'),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Zły format nazwy ulicy: tylko litery', regex='[a-zA-ZŻŹĆĄŚĘŃŁÓżźćąśęńłó]')], verbose_name='Nazwa ulicy'),
        ),
    ]
