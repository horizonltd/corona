# Generated by Django 2.2 on 2020-04-01 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HighestQualification',
            new_name='Qualification',
        ),
    ]