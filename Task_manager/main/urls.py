from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', Home.as_view(), name='home'),
    path('today/', today, name='today'),
    path('tomorrow/', tomorrow, name='tomorrow')
]
