# Generated by Django 2.2 on 2020-04-02 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0007_auto_20200402_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='picture',
            field=models.URLField(blank=True, default='', max_length=128, unique=True),
        ),
    ]
