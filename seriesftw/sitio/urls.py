from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'sitio.views.indice', name='sitio-indice'),
)

