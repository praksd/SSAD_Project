from __future__ import unicode_literals
from __future__ import unicode_literals
import datetime, os, sys
from PIL import Image
from django.db import models
from django.core.files import File
from django.conf import settings
from markdown import markdown
from django.utils import timezone
from datetime import datetime
from django.db import models
from tinymce.models import HTMLField



class Photo(models.Model):
        title = models.CharField(max_length=250,
                help_text='Maximum 250 characters.', blank=True)
        slug = models.SlugField(unique = True,
                help_text='Suggested value automatically generated from title. Must be unique.', null=True)
        summary = models.TextField(blank=True,
                help_text='An optional summary.')
        summary_html = models.TextField(editable=False, blank=True)
        date = models.DateTimeField(default=datetime.now)
        image = models.ImageField(upload_to='photos',
                help_text='Maximum resolution 800x600. Larger images will be resized.')
        thumb = models.ImageField(upload_to='photos', editable=False, null=True)

        class Meta:
                ordering = ['-date']
        def __unicode__(self):
                return self.title

        def save(self, force_insert=False, force_update=False):
                if self.summary:
                        self.summary_html = markdown(self.summary)
                super(Photo, self).save(force_insert, force_update)

                if self.image and not self.thumb:
                        #Set the thumbnail size and maximumsize
                        t_size = 200, 150
                        max_size = 800, 600
                        # Open the image that was uploaded.
                        im = Image.open(settings.MEDIA_ROOT + str(self.image))
                        # Compare the image size against the maximum size. If it is greater, the image will be resized.

        def get_absolute_url(self):
                return ('thaddeus_photo_detail', (),
                                { 'slug': self.slug })


class Album(models.Model):
    name = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)



class PressRelease(models.Model):
    Title = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    content = HTMLField()
