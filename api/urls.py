from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import TrialsHandler

trials_handler = Resource(TrialsHandler)

urlpatterns = patterns('',
   url(r'^trials/$', trials_handler),
   url(r'^trials/(?P<id>[\w]+)/', trials_handler),
)
