# Generated by Django 3.1.3 on 2020-12-30 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20201229_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='books'),
        ),
    ]
