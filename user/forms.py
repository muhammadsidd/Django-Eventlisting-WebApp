from django import forms
from user.models import UserManagement


class UserForm(forms.ModelForm):
    class Meta:
        model = UserManagement
        fields = '__all__'
        #exclude = ('user', 'date')

