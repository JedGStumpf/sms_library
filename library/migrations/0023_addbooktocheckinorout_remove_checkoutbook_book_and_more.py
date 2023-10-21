# Generated by Django 4.2.5 on 2023-10-18 16:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0022_alter_checkoutorin_check_in_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBookToCheckInOrOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='library.book')),
            ],
            options={
                'verbose_name_plural': 'Add Book to Check In/Out',
            },
        ),
        migrations.RemoveField(
            model_name='checkoutbook',
            name='book',
        ),
        migrations.RemoveField(
            model_name='checkoutorin',
            name='check_in',
        ),
        migrations.RemoveField(
            model_name='checkoutorin',
            name='check_out',
        ),
        migrations.AlterField(
            model_name='checkoutorin',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 1, 9, 16, 51, 316364)),
        ),
        migrations.DeleteModel(
            name='CheckinBook',
        ),
        migrations.DeleteModel(
            name='CheckoutBook',
        ),
        migrations.AddField(
            model_name='checkoutorin',
            name='add_book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='add_book', to='library.addbooktocheckinorout'),
        ),
    ]