from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def today(request):
    tasks_for_today = ("Сделать курсач", "Cделать АВС", "Сделать ТВИМС")
    return render(request, 'main/today.html', {'day': "сегодня", 'tasks': tasks_for_today})


def tomorrow(request):
    tasks_for_tomorrow = ("Cделать матешу", "Посмотреть ютуб", "Сходить на улицу")
    return render(request, 'main/tomorrow.html', {'day': "завтра", 'tasks': tasks_for_tomorrow})
