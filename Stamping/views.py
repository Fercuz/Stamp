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
from django.core.mail import EmailMultiAlternatives,EmailMessage


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
    info_send = False
    email = ""
    titulo = ""
    texto = ""

    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
            info_send = True
            email = form.cleaned_data['email']
            titulo = form.cleaned_data['titulo']
            texto = form.cleaned_data['texto']

            to_admin = 'soportestamping@gmail.com'
            html_content = "Información recibida de [%s]<br><br>Mensaje:<br><br>%s"%(email,texto)
            msg = EmailMultiAlternatives('Correo de Contacto', html_content,'from@server.com',[to_admin])
            msg.attach_alternative(html_content,'text/html')
            msg.send()
    else:
        form = Formulario()
    ctx = {'form':form, 'email':email,'titulo':titulo, 'texto':texto,'info_send':info_send}
    return render_to_response('contacto.html',ctx, context_instance=RequestContext(request))

def gracias(request):
    html = '<html><body><h1>Gracias por enviarnos su comentario!.</h1></body></html>'
    return HttpResponse(html)

def local(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

def ayuda(request):
    return render_to_response('help.html', context_instance=RequestContext(request))

def acerca(request):
    return render_to_response('help.html', context_instance=RequestContext(request))
