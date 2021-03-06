# Generated by Django 2.2 on 2019-08-31 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims', '0007_auto_20190813_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 31, 17, 18, 44, 997327)),
        ),
        migrations.AlterField(
            model_name='field',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 31, 17, 18, 44, 996331)),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 31, 17, 18, 45, 1316)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 31, 17, 18, 45, 1316)),
        ),
        migrations.AlterField(
            model_name='resultfields',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 31, 17, 18, 45, 319)),
        ),
        migrations.AlterField(
            model_name='sample',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 31, 17, 18, 44, 998325)),
        ),
        migrations.AlterField(
            model_name='sampletest',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 31, 17, 18, 44, 999322)),
        ),
        migrations.AlterField(
            model_name='section',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 31, 17, 18, 44, 993340)),
        ),
        migrations.AlterField(
            model_name='test',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 31, 17, 18, 44, 995334)),
        ),
    ]
