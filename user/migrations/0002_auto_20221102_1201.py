# Generated by Django 3.2.8 on 2022-11-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='count_music',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='user',
            name='penalizacion',
            field=models.IntegerField(default=0),
        ),
    ]
