from django.db import models
from __future__ import unicode_literals

class Album(models.Model):
    name = models.CharField(maxlength=128)
    slug = models.SlugField(prepopulate_from=("name",))
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)

class Photo(models.Model):
    title = models.CharField(maxlength=256)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False, width_field="width", height_field="height")
    album = models.ForeignKey(Album)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]

