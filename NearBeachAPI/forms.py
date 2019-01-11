from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from .models import *

class new_uuid_form(ModelForm):
    class Meta:
        model=api_uuid
        fields = {
            'api_description',
        }

class edit_uuid_form(ModelForm):
    class Meta:
        model=api_uuid
        fields = {
            'api_description',
        }