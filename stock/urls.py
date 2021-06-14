from typing import Pattern
from django import urls
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path('home/<int:value>', views.home, name='home')
]

