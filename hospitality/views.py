from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.
def home(request):
    return render_to_response('index.html', {
        'request': request,
        'page_id':'page1',
         'active': 'home',
    }, RequestContext(request, {}),)


def services(request):
    return render_to_response('services.html', {
        'request': request,
        'page_id':'page2',
         'active': 'services',
    }, RequestContext(request, {}),)


def booking(request):
    return render_to_response('booking.html', {
        'request': request,
        'page_id':'page3',
         'active': 'booking',
    }, RequestContext(request, {}),)


def rooms(request):
    return render_to_response('rooms.html', {
        'request': request,
        'page_id':'page4',
         'active': 'rooms',
    }, RequestContext(request, {}),)


def locations(request):
    return render_to_response('locations.html', {
        'request': request,
        'page_id':'page5',
         'active': 'locations',
    }, RequestContext(request, {}),)
