from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import *


class MusicAdmin(admin.ModelAdmin):
    list_display = ("name", "pub_date")

admin.site.register(Music, MusicAdmin)


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("name", "pub_date")

admin.site.register(Playlist, PlaylistAdmin)


class VerseAdmin(admin.ModelAdmin):
    list_display = ("name", "pub_date")

admin.site.register(Verse, VerseAdmin)


class ConcertAdmin(admin.ModelAdmin):
    list_display = ("name", "date_time", "pub_date")
    
admin.site.register(Concert, ConcertAdmin)



class TextPageFilter(admin.SimpleListFilter):
    title = _('Страница')
    parameter_name = 'page'

    def lookups(self, request, model_admin):

        return (
            ('index', _('Главная страница')),
            ('music', _('Песни')),
            ('verse', _('Стихи')),
            ('concerts', _('Концерты')),
            ('press', _('Пресс-релиз')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Главная страница':
            return queryset.filter(
                page = 'index'
            )
        if self.value() == 'Песни':
            return queryset.filter(
                page = 'index'
            )
        if self.value() == 'Стихи':
            return queryset.filter(
                page = 'index'
            )
        if self.value() == 'Концерты':
            return queryset.filter(
                page = 'index'
            )
        if self.value() == 'Пресс-релиз':
            return queryset.filter(
                page = 'index'
            )

class TextAdmin(admin.ModelAdmin):
    list_display = ("name", "page")
    list_filter = (TextPageFilter,)
    

admin.site.register(Text, TextAdmin)