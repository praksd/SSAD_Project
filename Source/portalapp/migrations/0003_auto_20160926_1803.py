# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0002_auto_20160926_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
