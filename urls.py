# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    
    (r'^loowar/$','apps.views.index'),
    (r'^status/$','apps.views.status'),
)


