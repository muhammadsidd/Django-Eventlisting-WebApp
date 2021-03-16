from django.urls import re_path, path
# from registeredevent.views import RegisterAnEvent
from registeredevent import views

app_name='registeredevent'

urlpatterns = [
    path('<int:event_id>/<int:user_id>', views.CreateRegister.as_view(), name='registeredevent'),
    path('register_event_confirmation/', views.test, name='register_event_confirm'),


]