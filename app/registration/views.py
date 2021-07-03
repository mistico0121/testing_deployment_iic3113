from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import Salesman
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

@method_decorator(login_required, name='dispatch')
class Salesman_list(ListView):
    model = Salesman
    def get_context_data(self, **kwargs):# con este metodo de la clase heredada se puede mandar un contexto normal con cualquier info
        context = super().get_context_data(**kwargs)
        context['salesmans'] = Salesman.objects.all()
        return context
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

@method_decorator(login_required, name='dispatch')
class SalesmanUpdate(UpdateView):
    model = Salesman
    fields = {'first_name','second_name'}
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        print("hol amno mono")
        salesman, created = Salesman.objects.get_or_create(user=self.request.user)
        print(salesman.user.username)
        print(salesman.user.password)
        return salesman
    def post(self, request, *args, **kwargs):     
        salesman = self.request.user
        name_element = dict(request.POST.lists())
        newname = name_element["cusername"][0]
        print(newname)
        salesman.username = newname
        salesman.save()
        
        return super().post(request, *args, **kwargs)
        
@method_decorator(login_required, name='dispatch')
def delete_user(request):
    context = {}
    print(request.user.username)
    try:
        u = request.user
        u.delete()
        context['msg'] = 'The user is deleted.'       
    except Salesman.DoesNotExist: 
        context['msg'] = 'User does not exist.'
    except Exception as e: 
        context['msg'] = e.message

    return HttpResponseRedirect(reverse('home'))
    

