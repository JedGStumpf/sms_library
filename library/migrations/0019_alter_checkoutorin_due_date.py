# Generated by Django 4.2.5 on 2023-10-15 18:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_alter_checkoutorin_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutorin',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 29, 11, 45, 32, 434397)),
        ),
    ]