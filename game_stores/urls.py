from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# API URLS 
from tastypie.api import Api

from api.api import GameResource, StoreResource
v1_api = Api(api_name='v1')
v1_api.register(GameResource())
v1_api.register(StoreResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'game_stores.views.home', name='home'),
    # url(r'^game_stores/', include('game_stores.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
