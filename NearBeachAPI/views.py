from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from NearBeach.models import project, organisation, customer
from django.http import JsonResponse
from django.core import serializers

from NearBeachAPI.models import *
from NearBeachAPI.forms import *

# Create your views here.
def data(request,destination):
    #Just sending back blanks at the moment
    t = loader.get_template('NearBeach/blank.html')
    c = {}

    #TEMP CODE#
    data_results = project.objects.filter(is_deleted="FALSE")
    data_json = serializers.serialize('json',data_results)
    return HttpResponse(data_json, content_type='application/json')

    """
    qs = SomeModel.objects.all()
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')
    """

    #return HttpResponse(t.render(c,request))
    #return HttpResponse(json.dumps(response_data), content_type="application/json")

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
    api_allowed_host_results = api_allowed_host.objects.filter(
        is_deleted="FALSE",
        api_uuid_id=api_uuid_id,
    )

    #Get Template
    t = loader.get_template('NearBeachAPI/edit_uuid.html')

    c = {
        'api_uuid_results': api_uuid_results,
        'new_allowed_host_form': new_allowed_host_form(),
        'api_allowed_host_results': api_allowed_host_results,
        'current_host': request.get_host(),
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
        'new_uuid_form': new_uuid_form(),
    }

    return HttpResponse(t.render(c,request))


def new_allowed_host(request,api_uuid_id):
    # Only in POST and super user
    if request.method == "POST" and request.user.is_superuser == True:
        form = new_allowed_host_form(request.POST)
        if form.is_valid():
            api_allowed_host_submit = api_allowed_host(
                allowed_host=form.cleaned_data['allowed_host'],
                change_user=request.user,
                api_uuid_id=api_uuid_id,
            )
            api_allowed_host_submit.save()

            #Return blank page
            t = loader.get_template('NearBeach/blank.html')
            c = {}
            return HttpResponse(t.render(c,request))
        else:
            print("FORM ERRORS!!!")
            print(form.errors)
            return HttpResponseBadRequest(form.errors)
    else:
        return HttpResponseBadRequest("Sorry - you can not do that here")


def new_uuid(request):
    # Only in POST and super user
    if request.method == "POST" and request.user.is_superuser == True:
        form = new_uuid_form(request.POST)
        if form.is_valid():
            #Create new uuid
            api_uuid_submit=api_uuid(
                api_description=form.cleaned_data['api_description'],
                change_user=request.user,
            )
            api_uuid_submit.save()

            #Send back blank page - AJAX will now allow us to render page
            t = loader.get_template('NearBeach/blank.html')
            c = {}
            return HttpResponse(t.render(c,request))
        else:
            return HttpResponseBadRequest(form.errors)
        #TEMP
        return HttpResponseRedirect(reverse('list_uuid'))
    else:
        return HttpResponseBadRequest("Nope - there is nothing here.")
