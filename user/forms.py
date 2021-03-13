from django import forms
from user.models import UserManagement
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        #exclude = ('user', 'date')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2', 'first_name', 'last_name', 'groups']

