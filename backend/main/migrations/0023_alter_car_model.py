# Generated by Django 4.1.3 on 2023-01-16 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_requestclient_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.DateField(verbose_name='مدل'),
        ),
    ]
