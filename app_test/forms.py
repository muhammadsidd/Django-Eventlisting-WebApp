from django import forms
from app_test.models import Eventtt


class EventForm(forms.ModelForm):
    class Meta:
        model = Eventtt
        fields = '__all__'

