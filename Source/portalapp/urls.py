from django.conf.urls import patterns,include,url
from . import views


urlpatterns = [
    url(r'^$',views.pressrelease_short, name='pressrelease_short'),
    url(r'^talk/(?P<pk>\d+)/part/$', views.talk_part, name='talk_part'),
    url(r'^talk/list/$', views.talks_list, name='talks_list'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^press/$',views.pressrelease,name='pressrelease'),
    url(r'^talk/new/$', views.talk_new, name='talk_new'),
    url(r'^talk/detail/$',views.talks_detail, name='talks_detail'),
    url(r'^talk/(?P<pk>\d+)/edit/$', views.talk_edit, name='talk_edit'),
    url(r'^album/(?P<pk>\d+)/view/$', views.photo_list, name='photo_list'),
    url(r'^gallery/$', views.album_list, name='album_list'),
    url(r'^event/$',views.event,name='events'),
    url(r'^press/(?P<pk>\d+)/release_unique/$',views.release_unique,name='release_unique'),
    url(r'^event/(?P<pk>\d+)/event_unique/$',views.event_unique,name='event_unique'),
    url(r'^tinyurl$', views.home,name='tinyurl'),
    url(r'^tinyurl/(?P<id>[a-zA-Z0-9])$',views.link),
    #url(r'^tinyurl/(?P<id>[a-zA-Z0-9])/stats$',views.stats),

]
