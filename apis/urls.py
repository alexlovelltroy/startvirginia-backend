from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       (r'^(?P<format>\w+)/companies/$', 'apis.views.companies'),
                       (r'^test$', 'apis.views.test'),

)
