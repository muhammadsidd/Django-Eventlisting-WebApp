from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from user.models import UserManagement
from user.forms import UserForm

class UserDetails (ListView):
    model = UserManagement
    template_name = 'user/user_List.html'
    context_object_name = 'user'

class UserCreate(LoginRequiredMixin,CreateView):
    model = UserManagement
    form_class = UserForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('user:user_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserCreate, self).form_valid(form)

class UserUpdate(LoginRequiredMixin,UpdateView):
    model = UserManagement
    fields = '__all__'
    template_name = 'user/user_update.html'
    success_url = reverse_lazy('user:user_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserUpdate, self).form_valid(form)

class UserDelete(DeleteView):
    model = UserManagement
    template_name = 'user/user_confirm_delete.html'
    success_url = reverse_lazy('user:user_list')
