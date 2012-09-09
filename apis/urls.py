from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       (r'^(?P<format>\w+)/companies/$', 'apis.views.companies'),
                       (r'^(?P<format>\w+)/resources/$', 'apis.views.resources'),
                       (r'^(?P<format>\w+)/events/$', 'apis.views.events'),
)
