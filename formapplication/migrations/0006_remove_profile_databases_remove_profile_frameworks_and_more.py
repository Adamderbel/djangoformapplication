# Generated by Django 4.2.3 on 2023-07-31 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapplication', '0005_profile_databases_profile_frameworks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='databases',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='frameworks',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='libraires',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='other',
        ),
    ]
