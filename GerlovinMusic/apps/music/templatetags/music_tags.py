from django import template
from music.models import Music, Playlist

register = template.Library()

@register.simple_tag()
def get_playlist_songs(playlist):
    return playlist.songs.all()

@register.simple_tag()
def get_concert_songs(concert):
    return concert.songs.all()