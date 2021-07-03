from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Device
from .forms import DeviceForm
from django.contrib.auth.decorators import login_required

@login_required
def device_index_view(request):
    queryset = Device.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "device/index.html", context)
  
@login_required
def device_show_view(request, id=id):
    obj = get_object_or_404(Device, id=id)
    obj.new_price = obj.price * (1 - obj.sale)
    obj.sale = obj.sale * 100
    context = {
        'object': obj
    }
    return render(request, "device/show.html", context)
  
@login_required
def device_create_view(request):
    form = DeviceForm(request.POST or None)
    if form.is_valid():
        fcc_form = form.save(commit=True)
        return redirect(reverse('point_of_sale-show', kwargs={'id': fcc_form.point_of_sale.id}))
    context = {
        'form': form
    }
    return render(request, "device/create.html", context)
  
@login_required
def device_update_view(request, id=id):
    obj = get_object_or_404(Device, id=id)
    form = DeviceForm(request.POST or None, instance=obj)
    if form.is_valid():
        fcc_form = form.save(commit=True)
        return redirect(reverse('point_of_sale-show', kwargs={'id': fcc_form.point_of_sale.id}))
    context = {
        'form': form
    }
    return render(request, "device/create.html", context)
  
@login_required
def device_delete_view(request, id):
    obj = get_object_or_404(Device, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect(reverse('point_of_sale-show', kwargs={'id': obj.point_of_sale.id}))
    context = {
        "object": obj
    }
    return render(request, "device/delete.html", context)
