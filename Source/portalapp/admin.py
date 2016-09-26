from django.contrib import admin
from .models import Register
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    #prepopulated_fields = { 'slug': ['title'] }

admin.site.register(Photo, PhotoAdmin)



admin.site.register(Register)

                                    
