# Generated by Django 2.2 on 2020-04-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0002_auto_20200402_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='ward',
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='geolocation',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='lga',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='prepared_Days_To_be_Involved',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='prepared_State_of_To_Be_Involved',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='profession',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='profession',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='qualification',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='qualification',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='specialization',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='specialization',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='state',
            field=models.CharField(default='', max_length=120),
        ),
    ]