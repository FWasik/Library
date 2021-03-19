# Generated by Django 3.1.3 on 2020-12-21 18:48

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20201201_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='num_building',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='num_door',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='post_code',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='street_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book', verbose_name='Książka'),
        ),
    ]
