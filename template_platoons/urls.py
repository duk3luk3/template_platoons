from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'template_platoons.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^platoons/', include('uo_template_platoons.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^users/(?P<username>\w+)$', 'template_platoons.views.user'),
)
