from django.shortcuts import render
from django.core.mail import send_mail
from .forms import *


from .models import Music

def index(request):

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
    return render(request,"music/index.html", {'form' : form})
