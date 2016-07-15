from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from Stamping import views
from django.conf.urls.static import static
import Stamping

urlpatterns = (
    
    url(r'^$', Stamping.views.index_view, name='index'),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^local/', Stamping.views.local_view, name='local'),
    url(r'^contacto/$', Stamping.views.contacto_view, name='contacto'),
    #url(r'^facturas/$', Stamping.views.factura_view, name='factura'),
    url(r'^facturas/pagina/(?P<pag>.*)/$', Stamping.views.factura_view, name='facturas'),
    url(r'^factura/(?P<id_fac>.*)/$', Stamping.views.factura_single_view, name='factura'),

    #url(r'^factura/page/(?P<pag>.*)/$', Stamp, name='pagina'),
) 
