from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lightwrite.views.home', name='home'),
     url(r'^(?P<wash>[a-zA-Z0-9_.-]+)$', 'lightwrite.texts.views.write'),
     url(r'^t/(?P<wash>[a-zA-Z0-9_.-]+)/$', 'lightwrite.texts.views.json_get_text'),
     url(r'^a/about/$', 'lightwrite.texts.views.about'),
     url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
     url(r'^$', 'lightwrite.texts.views.root'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

