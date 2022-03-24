from django.shortcuts import render
from django.shortcuts import redirect

from django.core.mail import send_mail
from .forms import *

form = ContactForm()

def index(request):
    return render(request,"index/index.html", {'form' : form})


def message(request):
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
            print('message has been sent')
        else:
            print ('error')
    return redirect(request.META.get('HTTP_REFERER'))
