# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from . import views

from django.views.generic import TemplateView, ListView, View
class IndexView(TemplateView):
    template_name = 'blog/base.html'

urlpatterns = [
    url(r'^home/$', IndexView.as_view(template_name='blog/base.html'), name="home"),
    url(r'^videoplay/$', views.videoplay, name="videoplay"),
    url(r'^vipplay/(?P<page>\d*)?$', views.vipplay, name="vipplay"),
]
