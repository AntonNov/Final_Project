from django.urls import path

from .views import *

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("today/", Today.as_view(), name="today"),
    path("tomorrow/", Tomorrow.as_view(), name="tomorrow"),
]
