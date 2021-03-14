from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from registration.registration import Registration
from event.models import Event
from .models import RegistrationItem
from .forms import RegistrationForm

def registration_create (request, event_id):
    event = get_object_or_404(Event, id=event_id)
    registration = RegistrationItem.objects.all()
    form = RegistrationForm()
    return render(request, 'registration/registration_create.html', {'event':event,
                                                                     'registration': registration,
                                                                     'form':form})

def registration_detail(request):
    registration = Registration(request)
    return render(request, 'registration/registration_detail.html', {'registration': registration})


def registration_adult_add(request, event_id):
    session_registration_obj = Registration(request)
    session_registration_obj.addnewAdult(get_object_or_404(Event, id= event_id))
    return redirect('registration:registration_create')

def registration_child_add(request, event_id):
    session_registration_obj = Registration(request)
    session_registration_obj.addnewChild(get_object_or_404(Event, id= event_id))
    return redirect('registration:registration_detail')

def registration_adult_remove(request, event_id):
    session_registration_obj = Registration(request)
    session_registration_obj.removeAdult(event_id)
    return HttpResponseRedirect(reverse_lazy('registration:registration_detail'))

def registration_child_remove(request, event_id):
    session_registration_obj = Registration(request)
    session_registration_obj.removeChild(event_id)
    return HttpResponseRedirect(reverse_lazy('registration:registration_detail'))

