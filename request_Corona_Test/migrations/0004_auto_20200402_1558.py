# Generated by Django 2.2 on 2020-04-02 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_Corona_Test', '0003_auto_20200401_1933'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Specialization',
        ),
        migrations.RemoveField(
            model_name='requestcoronatest',
            name='testRequestID',
        ),
        migrations.AlterField(
            model_name='material',
            name='material',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='requestcoronatest',
            name='dob',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='requestcoronatest',
            name='lga',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='requestcoronatest',
            name='name',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='requestcoronatest',
            name='note',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='requestcoronatest',
            name='polling_unit',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='requestcoronatest',
            name='preferedStateOfTest',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='requestcoronatest',
            name='state',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='requestcoronatest',
            name='time',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='requestcoronatest',
            name='ward',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.DeleteModel(
            name='Lga',
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.DeleteModel(
            name='Ward',
        ),
    ]
