# Generated by Django 4.2.5 on 2023-10-17 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_validemail_remove_customuser_needs_reset_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='validemail',
            options={'verbose_name_plural': 'Valid Emails'},
        ),
    ]
