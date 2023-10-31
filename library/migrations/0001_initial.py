# Generated by Django 4.2.5 on 2023-10-31 18:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50, null=True)),
                ('returned', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_first_name', models.CharField(help_text='Student First Name', max_length=100)),
                ('student_last_name', models.CharField(help_text='Student Last Name', max_length=100)),
                ('grade', models.IntegerField(choices=[(0, 'Kinder'), (1, '1st'), (2, '2nd'), (3, '3rd'), (4, '4th'), (5, '5th'), (6, '6th Only'), (7, '7th Only'), (8, '8th Only')])),
            ],
        ),
        migrations.CreateModel(
            name='CheckOutOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateField(blank=True, default=datetime.date(2023, 11, 14), null=True)),
                ('checked_out_on', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('order_returned', models.BooleanField(default=False, verbose_name='Order Completely Returned')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_order', to='library.student')),
            ],
            options={
                'verbose_name_plural': 'Check Out Orders',
            },
        ),
    ]
