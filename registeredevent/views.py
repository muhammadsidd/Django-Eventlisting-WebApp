from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from registeredevent.models import RegisteredEvent
from registeredevent.forms import RegistrationForm
from django.shortcuts import render

from django.http import HttpResponse


def test(request):
    users = RegisteredEvent.objects.all()
    return render(request, 'registeredevent/register_event_confirmation.html', {'users':users})

# class Confirmation(ListView):
#     model = RegisteredEvent
#     template_name = '/register_event_confirmation.html'

    
class CreateRegister(CreateView):

    model = RegisteredEvent
    form_class = RegistrationForm
    template_name = 'registeredevent/register_event.html'
    success_url = reverse_lazy('regesteredevent:register_event_confirm')

    def post(self, request, *args, **kwargs):
        # form = self.form_class(request.POST)
        print("-----")
        user_id = self.kwargs['user_id'] 
        print(self.kwargs['event_id'])


        print("-----")
        # if form.is_valid():
        #     # <process form cleaned data>
        #     return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': self.form_class,"user_id":user_id})
