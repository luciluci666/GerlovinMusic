from django.shortcuts import render
from django.core.mail import send_mail
from .forms import *

from GerlovinMusic.settings import STATIC_ROOT
import json
import os
from .models import Music

def index(request):
    json_path = song_json()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            text ='Имя: ' + str(form.cleaned_data['name']) + '\n' + 'Контакты: ' + str(form.cleaned_data['contact']) + '\n'+ 'Обращение: ' + str(form.cleaned_data['sometext']) + '\n'
            send_mail(
                'Новое заявка на сайте GerlovinMusic',
                text,
                'gerlovin.music@gmail.com',
                ['gerlovin.music@gmail.com'],
                fail_silently=False,
                )
        else:
            print ('error')
    form = ContactForm()
    return render(request,"music/index.html", {'form' : form, 'path' : json_path})


def song_json():    
    song_dict=[]
    all_songs = Music.objects.all()
    
    for song in all_songs:
        print(song.name)
        song_dict.append({
            "song" + str(song.id) :{"id" : str(song.id), "name" : song.name, "path" : str(song.audio_file)}
        })
    json_object = json.dumps(song_dict, indent = 4, ensure_ascii=False)

    path = os.path.join(STATIC_ROOT, "static_files", "js", "json", "songs.json")
    with open(path , "w", encoding="utf-8") as outfile:
        outfile.write(json_object)

    return path
