# Generated by Django 4.1.3 on 2022-12-31 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_requestclient_finish_loc'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestclient',
            name='finish_loc_lat',
            field=models.FloatField(blank=True, null=True, verbose_name='طول پایان'),
        ),
        migrations.AddField(
            model_name='requestclient',
            name='start_loc_lat',
            field=models.FloatField(blank=True, null=True, verbose_name='عرض شروع'),
        ),
        migrations.AddField(
            model_name='requestclient',
            name='start_loc_lon',
            field=models.FloatField(blank=True, null=True, verbose_name='طول شروع'),
        ),
        migrations.AddField(
            model_name='requestdriver',
            name='finish_loc_lat',
            field=models.FloatField(blank=True, null=True, verbose_name='طول پایان'),
        ),
        migrations.AddField(
            model_name='requestdriver',
            name='start_loc_lat',
            field=models.FloatField(blank=True, null=True, verbose_name='عرض شروع'),
        ),
        migrations.AddField(
            model_name='requestdriver',
            name='start_loc_lon',
            field=models.FloatField(blank=True, null=True, verbose_name='طول شروع'),
        ),
    ]
