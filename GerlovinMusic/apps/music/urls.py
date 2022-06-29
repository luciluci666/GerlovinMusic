from django.urls import path

from GerlovinMusic.apps.music import utils
from . import views

urlpatterns = [
    path('', views.index.index, name = 'index.index'),
    path('music/', views.music.index, name = 'music.index'),
    path('music/<id>', views.music.show, name = 'music.show'),
    path('verse/', views.verse.index, name = 'verse.index'),
    path('verse/<id>', views.verse.show, name = 'verse.show'),

    path('message', utils.MyPage.message, name = 'message'),   
]