
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template 
from django.template import Context
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from Stamping.models import *
from django.shortcuts import get_object_or_404
from django.template.context import RequestContext

def handler404(request):
    response = render_to_response('404.html', {},context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', {},context_instance=RequestContext(request))
    response.status_code = 500
    return response

def index(request):
    return render_to_response('index.html', context_instance = RequestContext(request))

def local(request):
    return render_to_response('home.html', context_instance = RequestContext(request))

def ayuda(request):
	return render_to_response('help.html', context_instance = RequestContext(request))

def acerca(request):
	return render_to_response('help.html', context_instance = RequestContext(request))


