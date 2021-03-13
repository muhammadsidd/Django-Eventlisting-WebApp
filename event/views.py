from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from event.models import Event, Category
from event.forms import EventForm, CategoryForm


class EventList(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'event/event_list.html'
    context_object_name = 'event'
    success_url = reverse_lazy('event:event_list')
    login_url = 'login'

    # this is a test
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventList, self).form_valid(form)


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event/event_create.html'
    success_url = reverse_lazy('event:event_List')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreate, self).form_valid(form)


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'event/category_new.html'
    success_url = reverse_lazy('event:event_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CategoryCreate, self).form_valid(form)


class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = '__all__'
    template_name = 'event/event_update.html'
    success_url = reverse_lazy('event:event_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventUpdate, self).form_valid(form)


class EventDelete(DeleteView, LoginRequiredMixin):
    model = Event
    template_name = 'event/event_confirm_delete.html'
    success_url = reverse_lazy('event:event_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventDelete, self).form_valid(form)


class EventDetail(DetailView):
    model = Event
    template_name = 'event/event_detail.html'
    context_object_name = 'event'
