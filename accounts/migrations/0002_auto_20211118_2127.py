# Generated by Django 3.2.9 on 2021-11-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='acc_point',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='curr_point',
            field=models.IntegerField(default=0),
        ),
    ]
