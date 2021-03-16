from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from rest_framework.generics import get_object_or_404

from event.models import Event
from registeredevent.models import RegisteredEvent
from registeredevent.forms import RegistrationForm
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect


def registration_create(request, event_id, user_id):
        print(event_id)
        print(user_id)
        
        # registration = RegisteredEvent.objects.all()
        form = RegistrationForm()
        return render(request, 'registeredevent/register_event_confirmation.html', {'form': form,'event_id':event_id, 'user_id':user_id})

def registration_confirm(request,event_id,user_id):
    if request.method == "POST":
        print("here")
        print(event_id)

        print(user_id)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user_id = user_id
            registration.event_id = event_id
            registration.save()
            # x = RegisteredEvent.total_value(event_id)
            # print(x)
            return HttpResponseRedirect(reverse('event:event_list'))


