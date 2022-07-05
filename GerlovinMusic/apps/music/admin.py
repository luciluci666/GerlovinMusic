from django.contrib import admin

from .models import *

admin.site.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ("name")

admin.site.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("name")

admin.site.register(Verse)
class VerseAdmin(admin.ModelAdmin):
    list_display = ("name")

admin.site.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ("name")
