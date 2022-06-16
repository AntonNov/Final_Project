from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("today/", Today.as_view(), name="today"),
    path("tomorrow/", Tomorrow.as_view(), name="tomorrow"),
    path('add/', Add.as_view(), name="add"),
    path('update/', Update.as_view(), name="update"),
    path('delete/', Delete.as_view(), name="delete"),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
]
