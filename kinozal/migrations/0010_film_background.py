# Generated by Django 4.1.1 on 2022-10-11 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinozal', '0009_alter_film_base_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to='background'),
        ),
    ]
