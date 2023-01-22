# Generated by Django 4.1.3 on 2022-12-30 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_requestclient_distance_requestdriver_distance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestclient',
            name='estimated_time',
            field=models.PositiveBigIntegerField(default=0, verbose_name='زمان تخمینی'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requestdriver',
            name='estimated_time',
            field=models.PositiveBigIntegerField(default=0, verbose_name='زمان تخمینی'),
            preserve_default=False,
        ),
    ]