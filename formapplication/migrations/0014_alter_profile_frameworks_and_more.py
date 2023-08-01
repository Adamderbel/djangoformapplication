# Generated by Django 4.2.3 on 2023-07-31 21:17

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('formapplication', '0013_alter_profile_more_about_your_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='frameworks',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Laravel', 'Laravel'), ('Angular', 'Angular'), ('Django', 'Django'), ('Flask', 'Flask'), ('Vue', 'Vue'), ('Others', 'Others')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='more_about_your_skills',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
