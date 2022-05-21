from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.views import View
import json
import os

from .models import *
from .forms import *
from GerlovinMusic.settings import STATIC_ROOT
from .utils import MyPage

form = ContactForm()

class index(MyPage):
    def index(request):
        MyPage.songs_json(Music)
        return render(request,"index/index.html", {'form' : form})


class music(MyPage):
    def music_index(request):
        MyPage.songs_json(Music)
        return render(request,"music/index.html", {'form' : form})