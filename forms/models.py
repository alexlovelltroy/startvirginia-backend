from django.db import models
from apis.models import Startup, Event, Resource
from django.forms import ModelForm

class CompanyForm(ModelForm):
    class Meta:
        model = Startup
        exclude = ('longitude','latitude')

class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ('longitude','latitude')

class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        exclude = ('longitude','latitude')
