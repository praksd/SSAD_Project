# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0011_delete_pressrelease'),
    ]

    operations = [
        migrations.CreateModel(
            name='PressRelease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=256)),
                ('summary', models.TextField(help_text='A summary for the archive.', blank=True)),
                ('slug', models.SlugField(help_text='Suggested value automatically generated from title. Must be unique.', unique=True, null=True)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(help_text="Kindly optimize the image <a href='http://optimizilla.com/'>here</a> before uploading", upload_to='coverphotos')),
            ],
        ),
    ]
