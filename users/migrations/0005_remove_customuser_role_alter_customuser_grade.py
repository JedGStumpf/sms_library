# Generated by Django 4.2.5 on 2023-10-26 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='role',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='grade',
            field=models.IntegerField(choices=[(0, 'Kinder'), (1, '1st'), (2, '2nd'), (3, '3rd'), (4, '4th'), (5, '5th'), (6, '6th Only'), (7, '7th Only'), (8, '8th Only'), (9, 'Middle School - 2 or more of: (6th, 7th, 8th)'), (10, 'All - For Substitutes and Office Staff Only')]),
        ),
    ]