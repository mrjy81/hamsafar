# Generated by Django 4.1.3 on 2023-01-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_driver_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='charge',
            field=models.PositiveIntegerField(default=0, verbose_name='اعتبار'),
            preserve_default=False,
        ),
    ]