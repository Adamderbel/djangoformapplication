# Generated by Django 4.2.3 on 2023-07-30 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapplication', '0002_profile_created_at_profile_situation'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='educational_level',
            field=models.CharField(blank=True, choices=[('', 'Educational Level'), ('Sans Bac', 'Sans Bac'), ('Bac +1 ', 'Bac +1'), ('Bac +2', 'Bac +2'), ('Bac +3', 'Bac +3'), ('Bac +4', 'Bac +4'), ('Bac +5', 'Bac +5'), ('Bac +6', 'Bac +6'), ('Bac +7', 'Bac +7'), ('other', 'other')], max_length=50, null=True),
        ),
    ]
