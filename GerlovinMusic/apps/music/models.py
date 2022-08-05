from tabnanny import verbose
from django.db import models

from tinymce.models import HTMLField


class Music(models.Model):
    name = models.CharField(
        'Название песни', max_length=100, null=True, blank=True)
    desc = models.CharField('Описание', max_length=250, null=True, blank=True)
    text = HTMLField('Текст песни', null=True, blank=True)
    audio_file = models.FileField(
        'Загрузить песню', blank=True, null=True, upload_to='Music')
    image_file = models.ImageField(
        'Загрузить постер', blank=True, null=True, upload_to='MusicPosters')
    pub_date = models.DateField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"



class Playlist(models.Model):
    name = models.CharField(
        'Название альбома', max_length=100, null=True, blank=True)
    desc = HTMLField('Описание', null=True, blank=True)
    image_file = models.ImageField(
        'Загрузить постер', blank=True, null=True, upload_to='PlaylistPosters')
    songs = models.ManyToManyField(Music)
    pub_date = models.DateField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Плэйлист"
        verbose_name_plural = "Плэйлисты"


class Verse(models.Model):
    name = models.CharField('Название', max_length=100, null=True, blank=True)
    desc = models.CharField('Описание', max_length=500, null=True, blank=True)
    text = HTMLField('Текси', null=True, blank=True)
    pub_date = models.DateField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Стих"
        verbose_name_plural = "Стихи"


class Concert(models.Model):
    name = models.CharField('Название', max_length=100, null=True, blank=True)
    place = models.CharField('Место проводения', max_length=500, null=True, blank=True)
    desc = HTMLField('Описание', null=True, blank=True)
    image_file = models.ImageField(
        'Загрузить постер', blank=True, null=True, upload_to='PlaylistPosters')
    video = models.CharField('Ссылка на видео (YouTube)',
                             max_length=500, null=True, blank=True)
    songs = models.ManyToManyField(Music)
    date_time = models.DateTimeField(
        ("Дата проведения"), auto_now=False, auto_now_add=False)
    pub_date = models.DateField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Концерт"
        verbose_name_plural = "Концерты"


class Text(models.Model):
    PAGES = (
        ('index', 'Главная страница'),
        ('music', 'Песни'),
        ('verse', 'Стихи'),
        ('concerts', 'Концерты'),
        ('press', 'Пресс-релиз'),
    )

    page = models.CharField('На какой странице находится текст?', max_length=300, choices = PAGES)
    name = models.CharField('Название', max_length=100, null=True, blank=True)
    text = HTMLField('Текст', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Текст"
        verbose_name_plural = "Тексты"