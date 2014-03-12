from django.conf.urls import patterns, url

from uo_template_platoons import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
    )
