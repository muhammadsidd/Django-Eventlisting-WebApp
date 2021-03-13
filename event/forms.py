from django import forms
from event.models import Event, Category


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
