# Generated by Django 4.1.3 on 2023-01-18 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_driver_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='charge',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='اعتبار'),
        ),
    ]
