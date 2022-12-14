# Generated by Django 4.1.1 on 2022-10-01 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinozal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='movie_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='trailer_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='film',
            name='duration',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='film',
            name='rating',
            field=models.FloatField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='release_year',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
