from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Task


class Home(ListView):
    model = Task
    template_name = "main/index.html"


class Day:
    model = Task
    login_url = "/admin/"


class Today(Day, LoginRequiredMixin, ListView):
    template_name = "main/today.html"
    date_name = "сегодня"
    tasks_for_today = Task.objects.filter(date_name=date_name)
    extra_context = {"day": date_name, "tasks": tasks_for_today}


class Tomorrow(Day, LoginRequiredMixin, ListView):
    template_name = "main/tomorrow.html"
    date_name = "завтра"
    tasks_for_tomorrow = Task.objects.filter(date_name=date_name)
    extra_context = {"day": date_name, "tasks": tasks_for_tomorrow}
