from django.conf.urls import url
from django.contrib import admin
from Stamping import views
import Stamping

urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^$', Stamping.views.index, name='index'),
    url(r'^local/', Stamping.views.local, name='local'),
    url(r'^contacto/$', Stamping.views.contacto, name='contacto'),
    url(r'^gracias/$', Stamping.views.gracias, name='gracias'),

)
