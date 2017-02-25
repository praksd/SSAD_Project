# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0013_googlenews_link_querynews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Twitternews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news', models.CharField(max_length=700)),
            ],
        ),
    ]
