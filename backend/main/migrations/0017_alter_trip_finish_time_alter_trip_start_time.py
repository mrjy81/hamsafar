# Generated by Django 4.1.3 on 2022-12-31 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_trip_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='finish_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ رسیدن'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ حرکت'),
        ),
    ]