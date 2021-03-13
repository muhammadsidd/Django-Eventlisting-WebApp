from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from event import views

app_name = 'event'
urlpatterns = [
    path('', views.EventList.as_view(), name='event_list'),
    path('<int:pk>/', views.EventDetail.as_view(), name='event_detail'),
    path('create/', views.EventCreate.as_view(), name='event_create'),
    path('<int:pk>/update/', views.EventUpdate.as_view(), name='event_update'),
    path('<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
    path('new_cat/', views.CategoryCreate.as_view(), name='category_new'),


]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)