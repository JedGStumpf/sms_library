# Generated by Django 4.2.5 on 2023-10-24 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0040_alter_checkoutorder_checked_out_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbook',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='library.checkoutorder'),
        ),
    ]
