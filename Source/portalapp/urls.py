from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^talk/(?P<pk>\d+)/part/$', views.talk_part, name='talk_part'),
    url(r'^press/$',views.pressrelease,name='pressrelease'),
    url(r'^talk/new/$', views.talk_new, name='talk_new'),
    url(r'^campus/$', views.campus, name='campus'),
    url(r'^cult/$', views.cult, name='cult'),
    url(r'^academics/$', views.acads, name='acads'),
]
