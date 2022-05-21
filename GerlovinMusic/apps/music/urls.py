from django.urls import path

from GerlovinMusic.apps.music import utils
from . import views

urlpatterns = [
    path('', views.index.index, name = 'index.index'),
    path('music/', views.music.music_index, name = 'music.index'),

    path('message', utils.MyPage.message, name = 'message'),   
]