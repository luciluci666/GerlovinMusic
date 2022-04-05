from django.db import models

class Music(models.Model):
    name = models.CharField('Название песни', max_length=100, null=True, blank=True)
    desc = models.CharField('Описание', max_length=250, null=True, blank=True)
    audio_file = models.FileField('Загрузить песню', blank=True, null=True, upload_to='media/music')
    pub_date = models.DateField()

class Playlist(models.Model):
    name = models.CharField('Название плэй-листа', max_length=100, null=True, blank=True)
    first = models.ForeignKey(Music, on_delete=models.CASCADE, related_name="first")
    second = models.ForeignKey(Music, on_delete=models.CASCADE, related_name="second")
    third = models.ForeignKey(Music, on_delete=models.CASCADE, related_name="third")
    fourth = models.ForeignKey(Music, on_delete=models.CASCADE, related_name="fourth")
    fiveth = models.ForeignKey(Music, on_delete=models.CASCADE, related_name="fiveth")
    sixth = models.ForeignKey(Music, on_delete=models.CASCADE, related_name="sixth")
    seventh = models.ForeignKey(Music, on_delete=models.CASCADE, related_name="seventh")
    eighth = models.ForeignKey(Music, on_delete=models.CASCADE, related_name="eighth")
    ninth = models.ForeignKey(Music, on_delete=models.CASCADE, related_name="ninth")
    tenth = models.ForeignKey(Music, on_delete=models.CASCADE, related_name="tenth")

    