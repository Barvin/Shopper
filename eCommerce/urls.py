import os
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'static/media')}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'static')}),

    url(r'^$', 'home.views.homePage'),    
    url(r'^products/$', 'products.views.products'),
    url(r'^products/(?P<slug>[-\w]+)/$', 'products.views.product_single'),
    url(r'^contact/$', 'contact.views.contactForm'),
    
    
)
