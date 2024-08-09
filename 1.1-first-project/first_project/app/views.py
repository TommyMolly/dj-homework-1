from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
from datetime import datetime

def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def current_time_view(request):
    current_time = datetime.now().strftime('%H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    workdir_files = os.listdir('.')
    files_list = ','.join(workdir_files)
    msg = f'Список файлов в рабочей директории: {files_list}'
    return HttpResponse(msg)
