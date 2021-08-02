import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):

    class Meta:
        model = Event
        fields = ('Category','title')