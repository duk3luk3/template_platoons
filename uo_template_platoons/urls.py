from django.conf.urls import patterns, url

from uo_template_platoons import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^periods/(?P<periodname>\w+)$', views.period_view),
    url(r'^edit/periods/(?P<periodname>\w+)$', views.period_edit),
    url(r'^new/periods$', views.period_edit, name='uo_template_platoons.views.new_period'),
    url(r'^branches/(?P<branchname>\w+)$', views.branch),
    url(r'^armies/(?P<armyname>.+)$', views.army),
    )
