# Generated by Django 4.1.1 on 2022-10-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinozal', '0010_film_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='description_en',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='film',
            name='title_en',
            field=models.CharField(default='', max_length=255),
        ),
    ]
