from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.http import HttpResponse


import random
import os

from .models import *
from .forms import *

from .utils import MyPage

form = ContactForm()

class index(MyPage):
    def index(request):
        MyPage.songs_json(Music)
        random_sogns = random.sample(list(Music.objects.all()), 3)

        return render(request, "index/index.html", {'form' : form, 'songs' : random_sogns})
      
    

class music(MyPage):
    def index(request):
        MyPage.songs_json(Music)
        songs = Music.objects.all().order_by("-id")
        playlists = Playlist.objects.all().order_by("-id")

        pl_buttons = []
        i = 0
        while True:
            i += 1
            pl_buttons.append(i)
            if i == playlists.__len__() - 1:
                break
            
        return render(request,"music/index.html", {'form' : form, 'songs' : songs, 'playlists' : playlists, 'pl_buttons' : pl_buttons})

    def show(request, id):
        song = Music.objects.get(pk = id)
        
        playlist = Playlist.objects.filter(songs = id)[:1][0]


        return render(request, "music/show.html", {'form' : form, 'song' : song, 'playlist' : playlist})



class verse(MyPage):
        def index(request):
            verses = Verse.objects.all().order_by("-id")
            return render(request,"verse/index.html", {'form' : form})

        def show(request, id):

            return render(request, "verse/show.html", {'form' : form})
