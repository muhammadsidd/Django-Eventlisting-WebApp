from django import forms

from .models import RegistrationItem

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationItem
        fields = '__all__'