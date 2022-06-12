from django.contrib import admin

from .models import Music, Playlist

admin.site.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ("name")

admin.site.register(Playlist)
