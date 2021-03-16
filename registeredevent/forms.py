from django import forms

from .models import RegisteredEvent

class RegistrationForm(forms.ModelForm):
    # firstname = forms.CharField(
    #     label='fisrt name',
    #     max_length=70,
    #     widget=forms.TextInput(),
    #     required=True,
    # );
    # lastname = forms.CharField(
    #     label='Last name',
    #     max_length=70,
    #     widget=forms.TextInput(),
    #     required=True,
    # );
    # email = forms.CharField(
    #     label='Email',
    #     max_length=70,
    #     widget=forms.EmailInput(),
    #     required=True,
    # );  
    class Meta:
        model = RegisteredEvent
        fields = '__all__'

