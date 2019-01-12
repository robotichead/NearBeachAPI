from django.contrib import admin
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.list_uuid, name='list_uuid'),
    re_path(r'^data/(?P<destination>["project","task","requirement","quote","kanban_board","opportunity","organisation","customer"]+)/$', views.data,name='data'),
    re_path(r'^delete_uuid/(?P<quote_uuid>[0-9A-Za-z_\-]+)', views.delete_uuid, name='delete_uuid'),
    re_path(r'^edit_uuid/(?P<api_uuid_id>[0-9A-Za-z_\-]+)', views.edit_uuid, name='edit_uuid'),
    re_path(r'^new_allowed_host/(?P<api_uuid_id>[0-9A-Za-z_\-]+)', views.new_allowed_host, name='new_allowed_host'),
    re_path(r'^new_uuid/',views.new_uuid,name='new_uuid'),
]