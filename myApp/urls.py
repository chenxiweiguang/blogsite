#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:duwujun

from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^test/$', views.test),
        url(r'^test1/$', views.test1),
        url(r'^index/$', views.index),
        url(r'^about/$', views.about),
        url(r'^gbook/$', views.gbook),
        url(r'^learn/$', views.learn),
        url(r'^manshenghuo/$', views.manshenghuo),
        url(r'^mbfx/$', views.mbfx),
        url(r'^index1/$', views.index1),
        url(r'^register/$', views.register),
        url(r'^singin/$', views.singin),
        url(r'^singout/$', views.singout),
            ]


