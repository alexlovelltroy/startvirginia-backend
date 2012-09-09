from django.core import serializers
from models import Startup, Event, Resource
from django.http import HttpResponse
from datetime import datetime

def companies(request,format='json'):
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = '*'
    if format == 'json':
        all_objects = Startup.objects.all().order_by('name')
        data = serializers.serialize('json', all_objects, ensure_ascii=False, stream=response)
    else: #Default
        response = "No Known Format."
    return response

def events(request,format='json'):
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = '*'
    if format == 'json':
        filt_objects = Event.objects.filter(when__gte=datetime.now())
        data = serializers.serialize('json', filt_objects, ensure_ascii=False, stream=response)
    else: #Default
        response = "No Known Format."
    return response

def resources(request,format='json'):
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = '*'
    if format == 'json':
        all_objects = Resource.objects.all().order_by('name')
        data = serializers.serialize('json', all_objects, ensure_ascii=False, stream=response)
    else: #Default
        response = "No Known Format."
    return response
    
        
