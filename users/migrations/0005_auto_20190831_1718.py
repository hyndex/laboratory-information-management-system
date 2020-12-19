# Generated by Django 2.2 on 2019-08-31 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190813_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 31, 17, 18, 45, 4309)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 31, 17, 18, 45, 4309)),
        ),
        migrations.AlterField(
            model_name='profilerole',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 31, 17, 18, 45, 9296)),
        ),
        migrations.AlterField(
            model_name='role',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 31, 17, 18, 45, 5306)),
        ),
        migrations.AlterField(
            model_name='rolepermission',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 31, 17, 18, 45, 8300)),
        ),
        migrations.AlterField(
            model_name='scope',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 31, 17, 18, 45, 7301)),
        ),
    ]