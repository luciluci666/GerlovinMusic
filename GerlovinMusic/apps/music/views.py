from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail

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

        return render(request,"index/index.html", {'form' : form, 'songs' : random_sogns})


class music(MyPage):
    def music_index(request):
        MyPage.songs_json(Music)
        return render(request,"music/index.html", {'form' : form})