from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from .models import *

class edit_uuid_form(ModelForm):
    class Meta:
        model=api_uuid
        fields = {
            'api_description',
        }

class new_allowed_host_form(ModelForm):
    class Meta:
        model=api_allowed_host
        fields = {
            'allowed_host',
        }

class new_uuid_form(ModelForm):
    class Meta:
        model=api_uuid
        fields = {
            'api_description',
        }

