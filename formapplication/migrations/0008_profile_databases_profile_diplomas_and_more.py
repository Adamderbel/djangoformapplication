# Generated by Django 4.2.3 on 2023-07-31 09:58

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('formapplication', '0007_remove_profile_diplomas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='databases',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('MySql', 'MySql'), ('Postgree', 'Postgree'), ('MongoDB', 'MongoDB'), ('Sqlite3', 'Sqlite3'), ('Oracle', 'Oracle'), ('Others', 'Others')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='diplomas',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='educational_level',
            field=models.CharField(blank=True, choices=[('', 'Educational Level'), ('Sans Bac', 'Sans Bac'), ('Bac +1 ', 'Bac +1'), ('Bac +2', 'Bac +2'), ('Bac +3', 'Bac +3'), ('Bac +4', 'Bac +4'), ('Bac +5', 'Bac +5'), ('Bac +6', 'Bac +6'), ('Bac +7', 'Bac +7'), ('other', 'other')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='frameworks',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Laravel', 'Laravel'), ('Angular', 'Angular'), ('Django', 'Django'), ('Flask', 'Flask'), ('Vue', 'Vue'), ('Others', 'Others')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='institutions',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Python', 'Python'), ('Javascript', 'Javascript'), ('Java', 'Java'), ('C++', 'C++'), ('Ruby', 'Ruby'), ('Others', 'Others')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='libraires',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Ajax', 'Ajax'), ('Jquery', 'Jquery'), ('Reactjs', 'Reactjs'), ('scikit-learn', 'scikit-learn'), ('TensorFlow', 'TensorFlow'), ('Others', 'Others')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='numberofdiplomas',
            field=models.CharField(blank=True, choices=[('', 'Number Of Diploma/Degree Obtained'), ('1 ', '1'), ('2 ', '2'), ('2 ', '2'), ('3', '3'), ('more than 3', 'more than 3')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='other',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Others', 'Others')], default='', max_length=50),
        ),
    ]