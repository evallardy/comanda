from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
     path('juego/', Bingo.as_view(), name='juego'),
]