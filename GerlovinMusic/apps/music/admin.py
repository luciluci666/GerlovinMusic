from django.contrib import admin

from .models import *

admin.site.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ("name")

admin.site.register(Playlist)

admin.site.register(Verse)
