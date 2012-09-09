from apis.models import Resource, Event, Startup
from forms.models import CompanyForm, ResourceForm, EventForm
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from dateutil import parser
import simplejson
import urllib, urllib2

def company(request):
    startup = Startup()
    form = CompanyForm(instance=startup)
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            state = form.cleaned_data['state']
            state = state.upper().strip()
            ok_states = ['VA','VIRGINIA']
            if not state in ok_states:
                return HttpResponseRedirect('http://startvirginia.com/onlyva.html')

            ##This pattern of manual update SUCKS (sorry) -- I couldn't get
            ##it to work without the latitude data which gets added later
                
            startup.name = form.cleaned_data['name']
            startup.founded = form.cleaned_data['founded']
            startup.url = form.cleaned_data['url']
            startup.jobs_url = form.cleaned_data['jobs_url']
            startup.industry = form.cleaned_data['industry']
            startup.description = form.cleaned_data['description']
            startup.employee_count = form.cleaned_data['employee_count']
            startup.twitter = form.cleaned_data['twitter']
            startup.linkedin = form.cleaned_data['linkedin']
            startup.hiring = form.cleaned_data['hiring']
            startup.admin_email = form.cleaned_data['admin_email']
            startup.street1 = form.cleaned_data['street1']
            startup.street2 = form.cleaned_data['street2']
            startup.city = form.cleaned_data['city']
            startup.state = form.cleaned_data['state']
            startup.zipcode = form.cleaned_data['zipcode']
            (latitude, longitude) = location_from_address(
                form.cleaned_data['street1'],
                form.cleaned_data['city'],
                form.cleaned_data['state'],
                form.cleaned_data['zipcode'])
            startup.latitude = latitude
            startup.longitude = longitude
            startup.save()
            return HttpResponseRedirect('http://startvirginia.com/thankyou.html')

    context = {
        'startup':startup,
        'form':form,
        'form_action': HttpRequest.build_absolute_uri(request,"/forms/company")
        }
    response = render_to_response('forms/company.html', context,
                                  context_instance=RequestContext(request))
    response['Access-Control-Allow-Origin'] = '*'

    return response
    
def location_from_address(street1,city,state,zipcode):
    API_URL = 'http://maps.googleapis.com/maps/api/geocode/json?'
    params = {'sensor': 'false',
              'address': "%s %s %s %s" % (street1, city, state, zipcode),
              }
    request = urllib2.urlopen(API_URL + urllib.urlencode(params))
    response = request.read()
    data = simplejson.loads(response)
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    return(latitude,longitude)

def support(request):
    form = ResourceForm()
    resource = Resource()
    context = {
        'form':form,
        }
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            ok_states = ['VA','VIRGINIA']
            state = form.cleaned_data['state']
            state = state.upper().strip()
            if not state in ok_states:
                return HttpResponseRedirect('http://startvirginia.com/onlyva.html')

            resource.name = form.cleaned_data['name']
            resource.resource_type = form.cleaned_data['resource_type']
            resource.description = form.cleaned_data['description']
            resource.url = form.cleaned_data['url']

            resource.street1 = form.cleaned_data['street1']
            resource.street2 = form.cleaned_data['street2']
            resource.city = form.cleaned_data['city']
            resource.state = state
            resource.zipcode = form.cleaned_data['zipcode']

            (latitude, longitude) = location_from_address(
                form.cleaned_data['street1'],
                form.cleaned_data['city'],
                form.cleaned_data['state'],
                form.cleaned_data['zipcode'])

            resource.latitude = latitude
            resource.longitude = longitude
            resource.save()
            return HttpResponseRedirect('http://startvirginia.com/thankyou.html')

    response = render_to_response('forms/support.html', context,
                                  context_instance=RequestContext(request))
    response['Access-Control-Allow-Origin'] = '*'
    return response

def event(request):
    form = EventForm()
    event = Event()
    context = {
        'form':form,
        }
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            ok_states = ['VA','VIRGINIA']
            state = form.cleaned_data['state']
            state = state.upper().strip()
            if not state in ok_states:
                return HttpResponseRedirect('http://startvirginia.com/onlyva.html')
            event.name = form.cleaned_data['name']
            event.description = form.cleaned_data['description']
            event.when = form.cleaned_data['when']
            event.url = form.cleaned_data['url']
            event.street1 = form.cleaned_data['street1']
            event.street2 = form.cleaned_data['street2']
            event.city = form.cleaned_data['city']
            event.state = state
            event.zipcode = form.cleaned_data['zipcode']
            (latitude, longitude) = location_from_address(
                form.cleaned_data['street1'],
                form.cleaned_data['city'],
                form.cleaned_data['state'],
                form.cleaned_data['zipcode'])
            
            event.latitude = latitude
            event.longitude = longitude
            event.save()
            return HttpResponseRedirect('http://startvirginia.com/thankyou.html')
        
    response = render_to_response('forms/event.html', context,
                                  context_instance=RequestContext(request))
    response['Access-Control-Allow-Origin'] = '*'
    return response

