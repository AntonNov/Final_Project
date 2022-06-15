from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import *
from .models import *


class Home(ListView):
    model = Task
    template_name = "main/index.html"


class BaseClass:
    model = Task
    login_url = "/admin/"


class Today(BaseClass, LoginRequiredMixin, ListView):
    template_name = "main/today.html"
    date_name = "сегодня"
    tasks_for_today = Task.objects.filter(date_name=date_name)
    extra_context = {"day": date_name, "tasks": tasks_for_today}


class Tomorrow(BaseClass, LoginRequiredMixin, ListView):
    template_name = "main/tomorrow.html"
    date_name = "завтра"
    tasks_for_tomorrow = Task.objects.filter(date_name=date_name)
    extra_context = {"day": date_name, "tasks": tasks_for_tomorrow}


@login_required
def add(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddTaskForm()
    return render(request, 'main/add.html', {'form': form})


class Update(BaseClass, LoginRequiredMixin, ListView):
    template_name = "main/update.html"


class Delete(BaseClass, LoginRequiredMixin, ListView):
    template_name = "main/delete.html"
