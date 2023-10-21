# Generated by Django 4.2.5 on 2023-10-12 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='grade',
            field=models.IntegerField(choices=[(0, 'Kinder'), (1, '1st'), (2, '2nd'), (3, '3rd'), (4, '4th'), (5, '5th'), (6, '6th'), (7, '7th'), (8, '8th'), (9, 'Middle School (6th, 7th, 8th)'), (10, 'All')], default=10, max_length=35),
        ),
    ]
