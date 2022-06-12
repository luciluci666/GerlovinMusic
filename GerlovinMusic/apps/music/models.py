from django.db import models

from tinymce.models import HTMLField


class Music(models.Model):
    name = models.CharField('Название песни', max_length=100, null=True, blank=True)
    desc = models.CharField('Описание', max_length=250, null=True, blank=True)
    text = HTMLField('Текст песни', null=True, blank=True)
    audio_file = models.FileField('Загрузить песню', blank=True, null=True, upload_to='Music')
    image_file = models.ImageField('Загрузить постер', blank=True, null=True, upload_to='MusicPosters')
    pub_date = models.DateField()

    def __str__(self):
        return f"{self.name}"

class Playlist(models.Model):
    name = models.CharField('Название альбома', max_length=100, null=True, blank=True)
    desc = HTMLField('Описание', null=True, blank=True)
    image_file = models.ImageField('Загрузить постер', blank=True, null=True, upload_to='PlaylistPosters')
    songs = models.ManyToManyField(Music)
    pub_date = models.DateField()

    def __str__(self):
        return f"{self.name}"

   