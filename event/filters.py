import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending','Ascending'),
        ('descending','Descending')
    )
    ordering = django_filters.ChoiceFilter(label="Ordering", choices= CHOICES, method='filter_by_order')

    class Meta:
        model = Event
        fields = {'Category':['icontains'],'title': ['icontains']}

    def filter_by_order(selfself,queryset,name,value):
        expression = 'created' if value == 'ascending' else'-created'
        return queryset.order_by(expression)
