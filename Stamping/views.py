from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template.context import RequestContext
# from django.shortcuts import HttpResponseRedirect
from Stamping.forms import Formulario
from django.core.mail import EmailMessage


def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def contacto(request):
    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
            asunto = 'Este es un mensaje de mi blog en DJANGO'
            mensaje = form.cleaned_data['mensaje']
            email = form.cleaned_data['email']

            ##pendiete
            mail = EmailMessage(asunto, mensaje,'fercuz@gmail.com', ['second@test.com', 'dsdsd@gmail.von'] )
            mail.send()
        return render_to_response('gracias.html', context_instance=RequestContext(request))
    else:
        form = Formulario()
    return render_to_response('contacto.html', {'form': form}, context_instance=RequestContext(request))

def gracias(request):
    html = '<html><body><h1>Gracias por enviarnos su comentario!.</h1></body></html>'
    return HttpResponse(html)

def local(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

def ayuda(request):
    return render_to_response('help.html', context_instance=RequestContext(request))

def acerca(request):
    return render_to_response('help.html', context_instance=RequestContext(request))
