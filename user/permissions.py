from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'User':
            print("here")
            return redirect('user:event_list')

        if group == 'Admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function
