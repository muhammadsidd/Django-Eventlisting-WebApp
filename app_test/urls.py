from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app_test import views

app_name = 'app_test'
urlpatterns = [
    # path('list/', views.EventList.as_view(), name='event_list'),
    path('', views.EventCreate.as_view(), name='event_create'),


]
