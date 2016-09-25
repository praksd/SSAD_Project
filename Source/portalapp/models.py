from __future__ import unicode_literals 
from django.db import models
from django.utils import timezone
from datetime import datetime
 

class Album(models.Model):     
    name = models.CharField(max_length=128)     
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False) 

class Photo(models.Model):     
    title = models.CharField(max_length=256)     
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    width = models.IntegerField(default=0)     
    height = models.IntegerField(default=0)     
    image = models.ImageField(null=False, blank=False, width_field="width", height_field="height")     
    album = models.ForeignKey(Album)     
    
    
    def __unicode__(self):         
        return self.title     
    
    class Meta:         
        ordering = ["-timestamp"]


class Register(models.Model):
        author = models.ForeignKey('auth.User')
        topic = models.CharField(max_length=200)
        abstract = models.TextField()
        created_date = models.DateTimeField(default=timezone.now)
        speaker = models.CharField(max_length=200)
        venue = models.CharField(max_length=200)
        on_date = models.DateTimeField(blank = False,default=datetime.now)
        bio = models.TextField()
        coordinator = models.CharField(max_length=200)

        def __str__(self):
            return self.speaker

