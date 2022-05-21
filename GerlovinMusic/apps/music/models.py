from django.db import models

class Music(models.Model):
    name = models.CharField('Название песни', max_length=100, null=True, blank=True)
    desc = models.CharField('Описание', max_length=250, null=True, blank=True)
    text = models.TextField('Текст песни', null=True, blank=True)
    audio_file = models.FileField('Загрузить песню', blank=True, null=True, upload_to='Music')
    image_file = models.ImageField('Загрузить постер', blank=True, null=True, upload_to='MusicPosters')
    pub_date = models.DateField()

