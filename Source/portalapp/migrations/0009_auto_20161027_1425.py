# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0008_pressrelease'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(help_text="Kindly optimize the image <a href='http://optimizilla.com/'>here</a> before uploading", upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(help_text="Kindly optimize the image <a href='http://optimizilla.com/'>here</a> before uploading", upload_to='eventphotos'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(help_text="Kindly optimize the image <a href='http://optimizilla.com/'>here</a> before uploading", upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='pressrelease',
            name='image',
            field=models.ImageField(help_text="Kindly optimize the image <a href='http://optimizilla.com/'>here</a> before uploading", upload_to='coverphotos'),
        ),
        migrations.AlterField(
            model_name='register',
            name='image',
            field=models.ImageField(help_text="Kindly optimize the image <a href='http://optimizilla.com/'>here</a> before uploading", upload_to='photos'),
        ),
    ]
