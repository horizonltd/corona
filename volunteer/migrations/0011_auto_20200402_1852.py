# Generated by Django 2.2 on 2020-04-02 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0010_auto_20200402_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='picture',
            field=models.ImageField(blank=True, upload_to='volunteer/'),
        ),
    ]
