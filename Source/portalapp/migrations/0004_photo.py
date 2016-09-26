# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0003_auto_20160926_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Maximum 250 characters.', max_length=250, blank=True)),
                ('slug', models.SlugField(help_text='Suggested value automatically generated from title. Must be unique.', unique=True, null=True)),
                ('summary', models.TextField(help_text='An optional summary.', blank=True)),
                ('summary_html', models.TextField(editable=False, blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(help_text='Maximum resolution 800x600. Larger images will be resized.', upload_to='photos')),
                ('thumb', models.ImageField(upload_to='photos', null=True, editable=False)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
