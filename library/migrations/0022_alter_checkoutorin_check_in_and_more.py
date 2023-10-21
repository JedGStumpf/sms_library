# Generated by Django 4.2.5 on 2023-10-18 16:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0021_alter_checkoutorin_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutorin',
            name='check_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checkin', to='library.checkinbook'),
        ),
        migrations.AlterField(
            model_name='checkoutorin',
            name='check_out',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checkout', to='library.checkoutbook'),
        ),
        migrations.AlterField(
            model_name='checkoutorin',
            name='date_checked_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checkoutorin',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 1, 9, 8, 15, 559391)),
        ),
    ]