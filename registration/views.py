from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView

from registration.models import Registration
from event.models import Event
from .forms import RegistrationForm


def registration_create (request, event_id):

    event = get_object_or_404(Event, id=event_id)
    registration = Registration.objects.all()
    form = RegistrationForm()
    return render(request, 'registration/registration_create.html', {'event':event,
                                                                     'registration': registration,
                                                                     'form':form})
def registration_confirm(request):
    if request.method == "POST":
        print("here")
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.save()
            return HttpResponseRedirect(reverse('registration:registration_list'))



def registration_list(request):
    registrations = Registration.objects.all()
    return render(request, 'registration/registration_list.html', {'registrations': registrations})


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
