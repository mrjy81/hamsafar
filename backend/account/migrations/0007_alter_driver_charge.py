# Generated by Django 4.1.3 on 2023-01-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_driver_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='charge',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='اعتبار'),
        ),
    ]
