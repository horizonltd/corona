# Generated by Django 2.2 on 2020-03-31 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='', max_length=100)),
                ('date', models.DateField(default=1994)),
                ('confirmed', models.CharField(default='', max_length=100)),
                ('death', models.CharField(default='', max_length=100)),
                ('recovered', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(default='', max_length=100)),
                ('date', models.DateField(default=1994)),
                ('confirmed', models.CharField(default='', max_length=100)),
                ('death', models.CharField(default='', max_length=100)),
                ('recovered', models.CharField(default='', max_length=100)),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='state', to='cases.Country')),
            ],
        ),
    ]
