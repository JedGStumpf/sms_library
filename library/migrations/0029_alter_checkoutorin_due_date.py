# Generated by Django 4.2.5 on 2023-10-22 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0028_alter_book_check_out_or_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutorin',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 13, 49, 9, 530578)),
        ),
    ]
