# Generated by Django 4.1.3 on 2022-12-30 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_phones_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_phone', to='account.phones', verbose_name='شماره تلفن'),
        ),
    ]