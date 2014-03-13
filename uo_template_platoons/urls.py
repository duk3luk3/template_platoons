from django.conf.urls import patterns, url

from uo_template_platoons import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^periods/(?P<periodname>\w+)$', views.period),
    url(r'^branches/(?P<branchname>\w+)$', views.branch),
    url(r'^armies/(?P<armyname>.+)$', views.army),
    )
