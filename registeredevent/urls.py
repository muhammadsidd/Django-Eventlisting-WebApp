from django.urls import re_path, path
# from registeredevent.views import RegisterAnEvent
from registeredevent import views

app_name='registeredevent'

urlpatterns = [
    path('<int:event_id>/<int:user_id>/<str:event_title>/<int:child_price>/<int:adult_price>/', views.registration_create, name='registeredevent'),
    path('register_event_confirmation/<int:event_id>/<int:user_id>', views.registration_confirm, name='register_confirm'),
    path('confirmation/<int:event_id>/<int:user_id>/', views.confirmation, name='confirmation'),

    # path('sucess/', views.confirmationSucess, name='confirm_success'),

]