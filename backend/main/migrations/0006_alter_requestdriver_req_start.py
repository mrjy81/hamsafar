# Generated by Django 4.1.3 on 2022-12-29 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_requestdriver_finish_loc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestdriver',
            name='req_start',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ شروع درخواست'),
        ),
    ]
