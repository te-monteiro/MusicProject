from django.contrib import admin

from music.models import Album, Artist

# Register your models here.
admin.site.register(Artist)
admin.site.register(Album)
