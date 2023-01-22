# Generated by Django 4.1.3 on 2023-01-02 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_driver_charge'),
        ('main', '0021_requestclient_text_address_finish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestclient',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_of_request', to='account.client', verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='requestdriver',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_of_request', to='account.driver', verbose_name='راننده'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='req_driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_request_trip', to='main.requestdriver'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='req_passenger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_request_trip', to='main.requestclient'),
        ),
    ]