# -*- coding: utf-8 -*-
from django.conf.urls import url

from wgg import views

base_urlpatterns = [
    url(r'^wgg/$', views.wgg_home, name='wgg_home'),
    url(r'^wgg/games/$', views.wgg_games, name='wgg_games'),
    url(r'^wgg/conflicts/$', views.wgg_conflicts, name='wgg_conflicts'),
]

urlpatterns = base_urlpatterns
