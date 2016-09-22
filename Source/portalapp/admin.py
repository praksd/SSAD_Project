from django.contrib import admin
from .models import Album, Photo

class AlbumAdmin(admin.ModelAdmin):
    list_display = ["name", "timestamp"]
    class Meta:
        model = Album

admin.site.register(Album, AlbumAdmin)



