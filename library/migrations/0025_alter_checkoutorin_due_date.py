# Generated by Django 4.2.5 on 2023-10-22 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0024_remove_checkoutorin_add_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutorin',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 11, 19, 48, 770706)),
        ),
    ]
