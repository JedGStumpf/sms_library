# Generated by Django 4.2.5 on 2023-10-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='needs_reset_email',
            field=models.BooleanField(default=True),
        ),
    ]
