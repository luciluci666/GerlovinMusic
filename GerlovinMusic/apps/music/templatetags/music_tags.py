from django import template
from music.models import Music, Playlist

register = template.Library()

@register.simple_tag()
def get_playlist_songs(playlist):
    return playlist.songs.all()