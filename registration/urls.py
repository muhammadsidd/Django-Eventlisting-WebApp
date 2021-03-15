from django.urls import re_path, path

from registration import views

app_name='registration'
urlpatterns = [
    re_path(r'^addadult/(?P<event_id>\d+)/$', views.registration_adult_add, name='registration_adult_add'),
    re_path(r'^addChild/(?P<event_id>\d+)/$', views.registration_child_add, name='registration_child_add'),
    re_path(r'^removeadult/(?P<event_id>\d+)/$', views.registration_adult_remove, name='registration_adult_remove'),
    re_path(r'^removechild/(?P<event_id>\d+)/$', views.registration_child_remove, name='registration_child_remove'),
    re_path(r'^create/(?P<event_id>\d+)/$', views.registration_create, name='registration_create'),
    re_path(r'^$', views.registration_list, name='registration_list'),
    path('confirm/', views.registration_confirm, name='registration_confirm'),
]