# Generated by Django 5.1.4 on 2024-12-15 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorgeneral',
            name='especialidad',
            field=models.CharField(default='Sin especialidad', max_length=100),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='ciudad',
            field=models.CharField(default='Sin ciudad', max_length=100),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='pais',
            field=models.CharField(default='Sin país', max_length=100),
        ),
    ]