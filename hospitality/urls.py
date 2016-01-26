from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^services/$', services, name='services'),
    url(r'^booking$', booking, name='booking'),
    url(r'^rooms$', rooms, name='rooms'),
    url(r'^locations$', locations, name='locations'),

]
