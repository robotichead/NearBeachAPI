from django.contrib import admin
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.list_uuid, name='list_uuid'),
    re_path(r'^delete_uuid/(?P<quote_uuid>[0-9A-Za-z_\-]+)', views.delete_uuid, name='delete_uuid'),
    re_path(r'^edit_uuid/(?P<quote_uuid>[0-9A-Za-z_\-]+)', views.edit_uuid, name='edit_uuid'),
    re_path(r'^new_uuid/',views.new_uuid,name='new_uuid'),
]