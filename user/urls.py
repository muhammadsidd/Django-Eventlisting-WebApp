from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from user import views

app_name = 'user'
urlpatterns = [
    path('', views.UserList.as_view(), name='user_List'),
    path('create/', views.UserCreate.as_view(), name='user_create'),
    path('<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('<int:pk>/delete/', views.UserDelete.as_view(), name='user_delete'),

]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)