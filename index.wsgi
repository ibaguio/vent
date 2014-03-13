import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/ubuntu/Django/vent_env/local/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/ubuntu/Django/vent')
sys.path.append('/home/ubuntu/Django/vent/vent')

os.environ['DJANGO_SETTINGS_MODULE'] = 'vent.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/home/ubuntu/Django/vent_env/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
