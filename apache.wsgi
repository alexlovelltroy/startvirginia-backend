import os
import sys
 
path = '/var/www/startvirginia'
if path not in sys.path:
    sys.path.insert(0, '/var/www/startvirginia')
    sys.path.insert(0, '/var/www/startvirginia/backend')
    
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()