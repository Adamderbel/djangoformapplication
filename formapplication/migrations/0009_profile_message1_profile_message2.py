# Generated by Django 4.2.3 on 2023-07-31 10:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('formapplication', '0008_profile_databases_profile_diplomas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='message1',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='message2',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
