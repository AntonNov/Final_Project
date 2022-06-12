from django.shortcuts import render
from django.views.generic import ListView

from .models import Task


# def index(request):
#     return render(request, 'main/index.html')

class Home(ListView):
    model = Task
    template_name = 'main/index.html'


def today(request):
    tasks_for_today = Task.objects.filter(date='2022-06-12')
    print(tasks_for_today)
    return render(request, 'main/today.html', {'day': "сегодня", 'tasks': tasks_for_today})


def tomorrow(request):
    tasks_for_tomorrow = Task.objects.filter(date='2022-06-13')
    print(tasks_for_tomorrow)
    return render(request, 'main/tomorrow.html', {'day': "завтра", 'tasks': tasks_for_tomorrow})

