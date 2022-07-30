from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.views import View
import json
import os

from .forms import *
from GerlovinMusic.settings import MEDIA_ROOT, STATIC_ROOT


class MyPage(View):
    def songs_json(music):    
        song_dict=[]
        all_songs = music.objects.all()
        
        for song in all_songs:
            print(song.audio_file)
            song_dict.append({
                "id" : str(song.id), "name" : song.name, "path" : str(song.audio_file), "poster" : str(song.image_file)
            })
        json_object = json.dumps(song_dict, indent = 4, ensure_ascii=False)

        path = os.path.join(STATIC_ROOT, "static_files", "js", "json", "songs.json")
        with open(path , "w", encoding="utf-8") as outfile:
            outfile.write(json_object)

        return path


    def message(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                text ='Имя: ' + str(form.cleaned_data['name']) + '\n' + 'Контакты: ' + str(form.cleaned_data['contact']) + '\n'+ 'Обращение: ' + str(form.cleaned_data['sometext']) + '\n'
                send_mail(
                    'Новое заявка на сайте GerlovinMusic',
                    text,
                    'gerl.adm@mail.ru',
                    ['gerlovin.music@gmail.com'],
                    fail_silently=False,
                    )
                print('message has been sent')
            else:
                print ('error')
        return redirect(request.META.get('HTTP_REFERER'))

