# Generated by Django 3.2.9 on 2021-11-18 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='reated',
            new_name='rated',
        ),
    ]
