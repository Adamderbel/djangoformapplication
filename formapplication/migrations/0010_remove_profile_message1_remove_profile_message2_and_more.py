# Generated by Django 4.2.3 on 2023-07-31 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapplication', '0009_profile_message1_profile_message2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='message1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='message2',
        ),
        migrations.AddField(
            model_name='profile',
            name='companies_you_worked_at',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='more_about_your_skills',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='why_should_we_hire_you',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='years_of_experience',
            field=models.CharField(blank=True, choices=[('', 'Years of experience'), ('NO experience', 'NO experience'), ('1 year', '1 year'), ('2 years', '2 years'), ('3 years', '3 years'), ('4 years', '4 years'), ('5 years', '5 years'), ('6 years', '6 years'), ('more', 'more')], max_length=50, null=True),
        ),
    ]
