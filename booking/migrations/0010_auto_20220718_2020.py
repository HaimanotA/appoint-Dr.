# Generated by Django 3.2.13 on 2022-07-18 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_auto_20220716_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availablehour',
            name='weekday',
        ),
        migrations.DeleteModel(
            name='Specialities',
        ),
        migrations.RemoveField(
            model_name='weekday',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_date',
        ),
        migrations.AlterField(
            model_name='patient',
            name='title',
            field=models.CharField(blank=True, choices=[('Dr', 'Dr.'), ('Prof', 'Prof.'), ('Mr', 'Mr.'), ('Mrs', 'Mrs.'), ('Ms', 'Ms.')], max_length=10, null=True, verbose_name='Title'),
        ),
        migrations.DeleteModel(
            name='AvailableHour',
        ),
        migrations.DeleteModel(
            name='WeekDay',
        ),
    ]
