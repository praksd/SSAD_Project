# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='on_date',
            new_name='date_and_time',
        ),
    ]
