from django.shortcuts import render

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from app_test.models import Eventtt
from app_test.forms import EventForm

class EventCreate(LoginRequiredMixin, CreateView):
    model = Eventtt
    form_class = EventForm
    template_name = 'event_create.html'
    success_url = reverse_lazy('event:event_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreate, self).form_valid(form)



