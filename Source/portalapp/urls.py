from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.talks_list, name='talks_list'),
    url(r'^talk/new/$', views.talk_new, name='talk_new'),
    url(r'^talk/detail/$',views.talks_detail, name='talks_detail'),
    url(r'^talk/(?P<pk>\d+)/edit/$', views.talk_edit, name='talk_edit'),
]
         
