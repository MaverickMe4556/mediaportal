from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.pressrelease_short, name='pressrelease_short'),
    url(r'^talk/(?P<pk>\d+)/part/$', views.talk_part, name='talk_part'),
    url(r'^talk/list/$', views.talks_list, name='talks_list'),
    url(r'^press/$',views.pressrelease,name='pressrelease'),
    url(r'^talk/new/$', views.talk_new, name='talk_new'),
    url(r'^talk/detail/$',views.talks_detail, name='talks_detail'),
    url(r'^talk/(?P<pk>\d+)/edit/$', views.talk_edit, name='talk_edit'),
    url(r'^all/$', views.all_photo, name='all_photo'),
    url(r'^campus/$', views.campus, name='campus'),
    url(r'^cult/$', views.cult, name='cult'),
    url(r'^academics/$', views.acads, name='acads'),
]
