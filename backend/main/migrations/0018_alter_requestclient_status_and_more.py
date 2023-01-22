# Generated by Django 4.1.3 on 2022-12-31 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_trip_finish_time_alter_trip_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestclient',
            name='status',
            field=models.CharField(choices=[('REQUESTED', 'REQUESTED'), ('STARTED', 'STARTED'), ('CANCELLED', 'CANCELLED'), ('COMPLETED', 'COMPLETED'), ('PROCESSED', 'PROCESSED')], default='REQUESTED', max_length=100),
        ),
        migrations.AlterField(
            model_name='requestdriver',
            name='status',
            field=models.CharField(choices=[('REQUESTED', 'REQUESTED'), ('STARTED', 'STARTED'), ('CANCELLED', 'CANCELLED'), ('COMPLETED', 'COMPLETED'), ('PROCESSED', 'PROCESSED')], default='REQUESTED', max_length=100),
        ),
        migrations.AlterField(
            model_name='trip',
            name='status',
            field=models.CharField(choices=[('REQUESTED', 'REQUESTED'), ('STARTED', 'STARTED'), ('CANCELLED', 'CANCELLED'), ('COMPLETED', 'COMPLETED'), ('PROCESSED', 'PROCESSED')], default='REQUESTED', max_length=100),
        ),
    ]
