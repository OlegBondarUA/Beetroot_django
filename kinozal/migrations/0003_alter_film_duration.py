# Generated by Django 4.1.1 on 2022-10-02 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinozal', '0002_film_movie_link_film_trailer_link_alter_actor_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='duration',
            field=models.CharField(max_length=50, null=True),
        ),
    ]