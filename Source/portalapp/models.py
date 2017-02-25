from __future__ import unicode_literals
import datetime, os, sys
from PIL import Image
from django.db import models
from django.core.files import File
from django.conf import settings
#from markdown import markdown
from django.utils import timezone
from datetime import datetime
from tinymce.models import HTMLField
from django import forms
#from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from django.utils.safestring import mark_safe
from django.utils.encoding import python_2_unicode_compatible


class Album(models.Model):
        title = models.CharField(max_length=250)
        date = models.DateTimeField(default=datetime.now)
        image = models.ImageField(upload_to='photos',
            help_text=mark_safe("Kindly optimize the image <a href='http://optimizilla.com/'>here</a> before uploading"))

        class Meta:
                ordering = ['-date']

        def __str__(self):
                return self.title


class Photo(models.Model):
        title = models.CharField(max_length=250,
                help_text='Maximum 250 characters.', blank=True)
        slug = models.SlugField(unique = True,
                help_text='Suggested value automatically generated from title. Must be unique.', null=True)
        caption = models.TextField(blank=True, max_length=250,
                help_text='An optional summary.')
        date = models.DateTimeField(default=datetime.now)
        image = models.ImageField(upload_to='photos',
                help_text=mark_safe("Kindly optimize the image <a href='http://optimizilla.com/'>here</a> before uploading"))
        album = models.ForeignKey(Album)

        class Meta:
                ordering = ['-date']
        def __unicode__(self):
                return self.title

        def get_absolute_url(self):
                return ('thaddeus_photo_detail', (),
                                { 'slug': self.slug })
        get_absolute_url = models.permalink(get_absolute_url)


class Register(models.Model):
        author = models.ForeignKey('auth.User')
        topic = models.CharField(max_length=200)
        abstract = models.TextField()
        created_date = models.DateTimeField(default=timezone.now)
        speaker = models.CharField(max_length=200)
        venue = models.CharField(max_length=200)
        date_and_time = models.DateTimeField(blank = False,default=datetime.now)
        bio = models.TextField()
        coordinator = models.CharField(max_length=200)
        image = models.ImageField(upload_to='photos',
                help_text=mark_safe("Kindly optimize the image <a href='http://optimizilla.com/'>here</a> before uploading"))

        def __str__(self):
            return self.speaker


class PressRelease(models.Model):
        Title = models.CharField(max_length=256)
        summary = models.TextField(blank=True, help_text='A summary for the archive.')
        slug = models.SlugField(unique = True, help_text='Suggested value automatically generated from title. Must be unique.', null=True)
        content=models.TextField()
        #timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
        date = models.DateTimeField(default=datetime.now)
        image = models.ImageField(upload_to='coverphotos',
            help_text=mark_safe("Kindly optimize the image <a href='http://optimizilla.com/'>here</a> before uploading"))

        def __str__(self):
            return self.Title


class Event(models.Model):
    Title=models.CharField(max_length=256)
    date=models.DateTimeField(default=datetime.now,blank=False)
    venue=models.CharField(max_length=512)
    content=models.TextField()
    image = models.ImageField(upload_to='eventphotos',
            help_text=mark_safe("Kindly optimize the image <a href='http://optimizilla.com/'>here</a> before uploading"))

    def __str__(self):
            return self.Title



class inNews(models.Model):
    Title=models.CharField(max_length=50)
    link=models.CharField(max_length=2048)
    date=models.DateTimeField(default=datetime.now,blank=False)

    def __str__(self):
         return self.Title

"""class FlatPageForm(forms.ModelForm):
    #fields
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = FlatPage
        fields="__all__"
"""

import string

_char_map = string.ascii_letters+string.digits

def index_to_char(sequence):
    return "tinyurl".join([_char_map[x] for x in sequence])


class Link(models.Model):
    link = models.URLField()
    hits = models.IntegerField(default=0)

    def __repr__(self):
        return "<Link (Hits %s): %s>"%(self.hits, self.link)

    def get_short_id(self):
        _id = self.id
        digits = []
        while _id > 0:
            rem = _id % 62
            digits.append(rem)
            _id /= 62
        digits.reverse()
        return index_to_char(digits)

    @staticmethod
    def decode_id(string):
        i = 0
        for c in string:
            i = i * 64 + _char_map.index(c)
        return i

@python_2_unicode_compatible
class Googlenews(models.Model):
    title = models.CharField(max_length=512)
    original_url = models.CharField(max_length=1024)
    pubdate = models.DateTimeField()
    imageurl = models.CharField(max_length=512,null=True)
    description = models.TextField()
    pub_agency = models.CharField(max_length=512)

    def __str__(self):
            return self.title

class Querynews(models.Model):
    query = models.CharField(max_length=300)
    num = models.IntegerField()

    def __str__(self):
            return self.query

@python_2_unicode_compatible
class Twitternews(models.Model):
    news = models.CharField(max_length=700)
    def __str__(self):
          return self.news
