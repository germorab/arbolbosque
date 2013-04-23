from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    url(r'^texto/$', 'arbol.bosque.views.crearTexto'),
    url(r'^categoria/$', 'arbol.bosque.views.crearCategoria'),
    url(r'^arbol/$', 'arbol.bosque.views.mostrarArbol'),
    
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    
    #url(r'^arbol/', include('arbol.foo.urls')),
    #url(r'^polls/$', 'polls.views.index'),
    #url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    #url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    #url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
