from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from rest_framework.generics import get_object_or_404

from event.models import Event
from registeredevent.models import RegisteredEvent
from registeredevent.forms import RegistrationForm
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect


def registration_create(request, event_id, user_id,event_title,child_price,adult_price):
        # print(event_id)
        # print(user_id)
        
        # registration = RegisteredEvent.objects.all()
        form = RegistrationForm()
        return render(request, 'registeredevent/register_event_confirmation.html', 
        {'form': form,'event_id':event_id, 
        'user_id':user_id,
        'event_title':event_title,
        'child_price':child_price,
        'adult_price':adult_price,

         
         })
def confirmationSucess(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def confirmation(request,event_id,user_id):
    print('test')
    
    if request.method == "POST":   
        form = RegistrationForm(request.POST)
        print("Out")
        if form.is_valid():
            print("okkk")
            registration = form.save(commit=False)
    
            registration.user_id = user_id
            registration.event_id = event_id
            print(registration)
            
            registration.save()
            # total_amount = registration.total_value(event_id)
            # registration.save()
            # return render(request,"carts/home.html",{})
            # return HttpResponseRedirect(reverse_lazy('adopcion:solicitud_listar'))
            return HttpResponse("You Have Confirmed Your Registeration.. you will get an email sooon")
            # return HttpResponseRedirect(reverse('registeredevent:confirm_success',))
    

def registration_confirm(request,event_id,user_id):
    if request.method == "POST":   
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            # registration.user_id = user_id
            # registration.event_id = event_id
            # print(event_id)
            total_amount = registration.total_value(event_id)
            # registration.save()
            # print(x)
            return render(request, 'registeredevent/confirmation.html',
             {"form":form,
             "user_id":user_id,
             "event_id":event_id,
             "total_amount":total_amount,
             })
            # return HttpResponseRedirect(reverse('registeredevent:confirmation', {"user_id":user_id,"event_id":event_id},))


