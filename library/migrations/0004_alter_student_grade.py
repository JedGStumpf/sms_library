# Generated by Django 4.2.5 on 2023-10-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_checkoutorder_due_date_alter_student_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(choices=[(0, 'Kinder'), (1, '1st'), (2, '2nd'), (3, '3rd'), (4, '4th'), (5, '5th'), (6, '6th Only'), (7, '7th Only'), (8, '8th Only')]),
        ),
    ]
