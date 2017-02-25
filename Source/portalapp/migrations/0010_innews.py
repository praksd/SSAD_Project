# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0009_auto_20161027_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='inNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=2048)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
