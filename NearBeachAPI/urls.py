from django.contrib import admin
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.list_uuid, name='list_uuid'),
]