from django.urls import path

from user import views

app_name = 'product'
urlpatterns = [
    path('', views.UserList.as_view(), name='product_list'),
    path('new/', views.UserCreate.as_view(), name='product_new'),
    path('<int:pk>/update/', views.UserUpdate.as_view(), name='product_update'),
    path('<int:pk>/delete/', views.UserDelete.as_view(), name='product_delete'),

]