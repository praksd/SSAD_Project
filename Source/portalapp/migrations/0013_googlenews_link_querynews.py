# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0012_pressrelease'),
    ]

    operations = [
        migrations.CreateModel(
            name='Googlenews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512)),
                ('original_url', models.CharField(max_length=1024)),
                ('pubdate', models.DateTimeField()),
                ('imageurl', models.CharField(max_length=512, null=True)),
                ('description', models.TextField()),
                ('pub_agency', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField()),
                ('hits', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Querynews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query', models.CharField(max_length=300)),
                ('num', models.IntegerField()),
            ],
        ),
    ]
