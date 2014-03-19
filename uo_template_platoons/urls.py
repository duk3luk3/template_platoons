from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, user_passes_test

from uo_template_platoons import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^periods/(?P<periodname>\w+)$', views.period_view),
    #url(r'^edit/periods/(?P<periodname>\w+)$', views.period_edit),
    #url(r'^new/periods$', views.period_edit, name='uo_template_platoons.views.new_period'),
    
    url(r'^branches/create$', login_required(views.BranchCreateView.as_view()), name='uo_template_platoons.views.new_branch'),
    url(r'^branches/(?P<pk>\d+)/edit$', login_required(views.BranchEditView.as_view()), name='uo_template_platoons.views.edit_branch'),
    url(r'^branches/(?P<pk>\d+)/delete$', login_required(views.BranchDeleteView.as_view()), name='uo_template_platoons.views.delete_branch'),
    url(r'^branches/(?P<branchname>\w+)$', views.branch),

    url(r'^periods/create$', login_required(views.PeriodCreateView.as_view()), name='uo_template_platoons.views.new_period'),
    url(r'^periods/(?P<pk>\d+)/edit$', login_required(views.PeriodEditView.as_view()), name='uo_template_platoons.views.edit_period'),
    url(r'^periods/(?P<pk>\d+)/delete$', login_required(views.PeriodDeleteView.as_view()), name='uo_template_platoons.views.delete_period'),
    url(r'^periods/(?P<periodname>\w+)$', views.period),
    
    url(r'^armies/create$', login_required(views.ArmyCreateView.as_view()), name='uo_template_platoons.views.new_army'),
    url(r'^armies/(?P<pk>\d+)/edit$', login_required(views.ArmyEditView.as_view()), name='uo_template_platoons.views.edit_army'),
    url(r'^armies/(?P<pk>\d+)/delete$', login_required(views.ArmyDeleteView.as_view()), name='uo_template_platoons.views.delete_army'),
    url(r'^armies/(?P<armyname>.+)$', views.army),
    )
