from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^talk/list/$', views.talks_list, name='talks_list'),
    url(r'^press/$',views.index,name='index'),
    url(r'^talk/new/$', views.talk_new, name='talk_new'),
    url(r'^talk/detail/$',views.talks_detail, name='talks_detail'),
    url(r'^talk/(?P<pk>\d+)/edit/$', views.talk_edit, name='talk_edit'),
    url(r'^gallery/$', views.photo_list, name='photo_list')
]
