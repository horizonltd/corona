# Generated by Django 2.2 on 2020-04-01 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request_Corona_Test', '0002_remove_requestcoronatest_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='requestcoronatest',
            name='lga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteers', to='request_Corona_Test.Lga'),
        ),
        migrations.AlterField(
            model_name='requestcoronatest',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteers', to='request_Corona_Test.State'),
        ),
        migrations.AlterField(
            model_name='requestcoronatest',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteers', to='request_Corona_Test.Ward'),
        ),
    ]