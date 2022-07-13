from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.http import HttpResponse


import random
import os
import datetime

from .models import *
from .forms import *

from .utils import MyPage

form = ContactForm()

class index(MyPage):
    def index(request):
        MyPage.songs_json(Music)
        random_sogns = random.sample(list(Music.objects.all()), 3)

        text_list = [Text.objects.get(name = "Главный (ИНДЕКС)"),
            Text.objects.get(name = "Песни"),
            Text.objects.get(name = "Фотографии с концертов"),
        ]

        return render(request, "index/index.html", {'form' : form, 'songs' : random_sogns, 'text_list' : text_list})
      
    

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

        return render(request,"verse/index.html", {'form' : form, 'verses' : verses})

    def show(request, id):
        verse = Verse.objects.get(pk = id)

        return render(request, "verse/show.html", {'form' : form, 'verse' : verse})


class concert(MyPage):
    def index(request):
        concerts = Concert.objects.all().order_by("-id")

        startDate = datetime.date(2000, 1, 1 )
        endDate = datetime.date(2100, 1, 1 )
        now = datetime.date.today()
        performance = Concert.objects.filter(date_time__range=[now, endDate] ).order_by("-date_time")
        concerts = Concert.objects.filter(date_time__range=[startDate, now] ).order_by("-date_time")

        text_list = [Text.objects.get(name = "Главный (КОНЦЕРТЫ)"),
            Text.objects.get(name = "Первый концерт"),
        ]

        return render(request,"concert/index.html", {'form' : form, 'concerts' : concerts, 'performance' : performance, 'text_list' : text_list})

    def show(request, id):
        concert = Concert.objects.get(pk = id)

        now = datetime.date.today()
        concert_date = datetime.date(concert.date_time.year, concert.date_time.month , concert.date_time.day)
        if(concert_date > now):
            performance = True
        else:
            performance = False
            
        return render(request, "concert/show.html", {'form' : form, 'concert' : concert, 'performance' : performance})


class press(MyPage):
    def index(request):
        text_list = [Text.objects.get(name = "Главный (ПР)"),
            Text.objects.get(name = "Наша история (1)"),
            Text.objects.get(name = "Наша история (2)"),
            Text.objects.get(name = "Наша команда"),
            Text.objects.get(name = "Наша цель"),
        ]
     
        return render(request, "press/index.html", {'form' : form, 'text_list' : text_list})
