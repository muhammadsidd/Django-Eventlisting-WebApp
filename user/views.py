from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from user.models import UserManagement,Role
from user.forms import UserForm, CreateUserForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class UserList (LoginRequiredMixin,ListView):
    model = User
    template_name = 'user/user_List.html'
    context_object_name = 'users'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserList, self).form_valid(form)

class UserCreate(LoginRequiredMixin,CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('user:user_List')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserCreate, self).form_valid(form)

class UserUpdate(LoginRequiredMixin,UpdateView):
    model = User
    form_class = CreateUserForm
    template_name = 'user/user_update.html'
    success_url = reverse_lazy('user:user_List')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserUpdate, self).form_valid(form)

class UserDelete(LoginRequiredMixin,DeleteView,):
    model = User
    template_name = 'user/user_confirm_delete.html'
    success_url = reverse_lazy('user:user_List')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserDelete, self).form_valid(form)

def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form' : form}
    return render(request, 'register.html', context)
