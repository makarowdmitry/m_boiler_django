# -*- coding: utf-8 -*-
from django.conf.urls import include, url, patterns
from django.contrib import admin
from item.views import *
# from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^filter/', filter_reuest),
    url(r'^$', index),
]
