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
from Stamping.forms import Contacto_Form
from django.core.mail import EmailMultiAlternatives,EmailMessage
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.forms import inlineformset_factory
from Stamping.models import *
from django.db import connection

def index_view(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def local_view(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

def contacto_view(request):
    info_send = False
    email = ""
    titulo = ""
    texto = ""

    if request.method == 'POST':
        form = Contacto_Form(request.POST)
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
        form = Contacto_Form()
    ctx = {'form':form, 'email':email,'titulo':titulo, 'texto':texto,'info_send':info_send}
    return render_to_response('contacto.html',ctx, context_instance=RequestContext(request))


@staff_member_required
def factura_view(request,pag):

    cliente_lst = Detalleventa.objects.all().filter(codigo_venta=pag)

    pag = Paginator(cliente_lst,1)

    try:
        page = int(pag)
    except:
        page = 1
    try:
        data = pag.page(page)
    except (EmptyPage,InvalidPage):
        data = pag.page(pag.num_pages)

    return render_to_response('factura/factura.html',{'dt': data,'vn': cliente_lst},context_instance=RequestContext(request))

def factura_single_view(request, id_fac):
    factura = Detalleventa.objects.get(codigo_detalle_venta=id_fac)
    return render_to_response('factura/singlefactura.html', {'factura': factura}, context_instance=RequestContext(request))

# Handlers Errors

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response

