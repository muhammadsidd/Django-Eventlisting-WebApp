import django_filters
from django.contrib.auth import authenticate, get_user_model
from django_filters import DateFilter, CharFilter

user = get_user_model()

class UserFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name= "date_joined", lookup_expr='gte')
    end_date = DateFilter(field_name="date_joined", lookup_expr='lte')
    # note = CharFilter(field_name='note',lookup_expr = 'icontains')

    class Meta:
        model = user
        fields = ('groups','username',)
        # field = {'title':['icontains'],
        #          'body':['icontains']} for char values look up that cotains the word not exact value
        # exclude =  ['date_created']
        # fields = '__all__'

