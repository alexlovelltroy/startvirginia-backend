from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       (r'^company$', 'forms.views.company'),
                       (r'^support$', 'forms.views.support'),
                       (r'^event$',  'forms.views.event'),

)
