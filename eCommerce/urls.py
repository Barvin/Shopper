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
    (r'^about/', 'home.views.aboutPage'),
    
    url(r'^products/$', 'products.views.products'),
    url(r'^products/(?P<slug>[-\w]+)/$', 'products.views.product_single'),
    url(r'^products/(?P<slug>[-\w]+)/add$', 'cart.views.add'),
    url(r'^contact/$', 'contact.views.contactForm'),
    url(r'^cart/$', 'cart.views.view'),
    url(r'^cart/delete$', 'cart.views.delete'),

    
    
)
