from django.core import serializers
from models import Startup, Event, Resource, Address
from django.http import HttpResponse

def companies(request,format='json'):
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = '*'
    if format == 'json':
        all_objects = list(Startup.objects.all())
        all_objects.extend(list(Address.objects.all()))
        data = serializers.serialize('json', all_objects, ensure_ascii=False, stream=response)
    else: #Default
        response = "No Known Format."
    return response
        
def test(request,parameter):
    return HttpResponse("Hello World.")
