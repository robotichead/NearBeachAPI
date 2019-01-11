from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from NearBeachAPI.models import *

# Create your views here.
def delete_uuid(request,api_uuid_id):
    #Only super user and POST
    if request.method == "POST" and request.user.is_superuser == True:
        api_uuid_update = api_uuid.objects.get(api_uuid_id=api_uuid_id)
        api_uuid_update.change_user = request.user
        api_uuid_update.is_deleted = "FALSE"
        api_uuid_update.save()

        #Go to the UUID list
        return HttpResponseRedirect(reverse('list_uuid'))
    else:
        return HttpResponseBadRequest("You can not pass!")


def edit_uuid(request,api_uuid_id):
    #Only super user
    if request.user.is_superuser == False:
        return HttpResponseBadRequest("Sorry - you do not have permission to see these pages")

    #Get Data
    api_uuid_results = api_uuid.objects.get(api_uuid_id=api_uuid_id)

    #Get Template
    t = loader.get_template('NearBeachAPI/edit_uuid.html')

    c = {
        'api_uuid_results': api_uuid_results,
    }

    return HttpResponse(t.render(c,request))


def list_uuid(request):
    #only allow super users
    if request.user.is_superuser == False:
        return HttpResponseBadRequest("Sorry - you do not have permission to see these pages")

    #Get data
    api_uuid_results = api_uuid.objects.filter(
        is_deleted="FALSE",
    )

    #Load the UUID Lists
    t = loader.get_template('NearBeachAPI/list_uuid.html')

    c = {
        'api_uuid_results': api_uuid_results,
    }

    return HttpResponse(t.render(c,request))


def new_uuid(request):
    # only allow super users
    if request.user.is_superuser == False:
        return HttpResponseBadRequest("Sorry - you do not have permission to see these pages")

    # Get Data

    # Load the new uuid
    t = loader.get_template('NearBeachAPI/new_uuid.html')

    c = {}

    return HttpResponse(t.render(c,request))