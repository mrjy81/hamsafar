# Generated by Django 4.1.3 on 2022-12-29 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_driver_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phones',
            name='phone',
            field=models.CharField(max_length=10, unique=True, verbose_name='شماره تلفن'),
        ),
    ]