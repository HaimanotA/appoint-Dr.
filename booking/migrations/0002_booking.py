# Generated by Django 3.2.13 on 2022-06-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('mrs', 'Mrs'), ('mr', 'Mr')], max_length=10, verbose_name='Gender')),
                ('title', models.CharField(blank=True, choices=[('Dr', 'Dr.'), ('Prof', 'Prof.')], max_length=10, verbose_name='Title')),
                ('forename', models.CharField(blank=True, max_length=20, verbose_name='First name')),
                ('surname', models.CharField(blank=True, max_length=20, verbose_name='Last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=256, verbose_name='Phone')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('booking_id', models.CharField(blank=True, max_length=100, verbose_name='Booking ID')),
            ],
        ),
    ]
