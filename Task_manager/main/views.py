from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import *
from .models import *


class Home(ListView):
    model = Task
    template_name = "main/index.html"


class BaseClass(ListView):
    model = Task
    login_url = reverse_lazy('home')


class Today(BaseClass, LoginRequiredMixin):
    template_name = "main/today.html"
    date_name = "сегодня"
    tasks_for_today = Task.objects.filter(date_name=date_name)
    extra_context = {"day": date_name, "tasks": tasks_for_today}


class Tomorrow(BaseClass, LoginRequiredMixin):
    template_name = "main/tomorrow.html"
    date_name = "завтра"
    tasks_for_tomorrow = Task.objects.filter(date_name=date_name)
    extra_context = {"day": date_name, "tasks": tasks_for_tomorrow}


class Add(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('home')
    form_class = AddTaskForm
    template_name = 'main/add.html'
    success_url = reverse_lazy('home')


class Update(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('home')
    template_name = "main/update.html"


class Delete(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('home')
    template_name = "main/delete.html"


class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
