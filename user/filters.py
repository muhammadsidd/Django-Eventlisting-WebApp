import django_filters
from django.contrib.auth import authenticate, get_user_model

user = get_user_model()

class UserFilter(django_filters.FilterSet):

    class Meta:
        model = user
        fields = '__all__'

