# Generated by Django 4.1.3 on 2022-12-31 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_trip_req_driver_trip_req_passenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestclient',
            name='text_address_start',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
    ]
