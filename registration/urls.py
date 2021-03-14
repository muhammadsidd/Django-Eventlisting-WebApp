from django.urls import re_path

from registration import views

app_name='registration'
urlpatterns = [
    re_path(r'^$', views.registration_detail, name='registration_detail'),
    re_path(r'^addadult/(?P<event_id>\d+)/$', views.registration_adult_add, name='registration_add_adult'),
    re_path(r'^addChild/(?P<event_id>\d+)/$', views.registration_child_add, name='registration_add_child'),
    re_path(r'^removeadult/(?P<product_id>\d+)/$', views.registration_adult_remove, name='registration_remove_adult'),
    re_path(r'^removechild/(?P<product_id>\d+)/$', views.registration_child_remove, name='registration_remove_child'),
]