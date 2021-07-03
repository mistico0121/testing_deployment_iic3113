from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Store
from point_of_sales.models import PointOfSale
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
@method_decorator(login_required, name='dispatch')
class Store_list(ListView):
    model = Store
    def get_context_data(self, **kwargs):# con este metodo de la clase heredada se puede mandar un contexto normal con cualquier info
        context = super().get_context_data(**kwargs)
        context['stores'] = Store.objects.all()
        return context
@login_required
def store_show_view(request, id=id):
    store = get_object_or_404(Store, id=id)
    point_of_sales = store.pointofsale_set.all()
    context = {
        'store': store,
        'point_of_sales': point_of_sales,
    }
    return render(request, "stores/store_detail.html", context)
@method_decorator(login_required, name='dispatch')
class Store_create(CreateView):
    model = Store
    fields = ['name','description']
    widgets = {}
    def get_success_url(self):
        return reverse('store-index')
@method_decorator(login_required, name='dispatch')
class Store_update(UpdateView):
    model = Store
    fields = ['name','description']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse('store-index')
@method_decorator(login_required, name='dispatch')
class Store_delete(DeleteView):
    model = Store
    success_url = reverse_lazy('store-index')
    def get(self, *args, **kwargs):
        return self.post( *args, **kwargs)
    