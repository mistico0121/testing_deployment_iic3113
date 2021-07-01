from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import PointOfSale
from .forms import PointOfSaleForm
from devices.models import Device
from attendance_tablets.models import AttendanceTablet
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@login_required
def point_of_sale_index_view(request):
    queryset = PointOfSale.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "point_of_sales/index.html", context)
@login_required
def point_of_sale_show_view(request, id=id):
    obj = get_object_or_404(PointOfSale, id=id)
    devices = obj.device_set.all()
    attendance_tablets = obj.attendancetablet_set.all()
    context = {
        'object': obj,
        'devices': devices,
        'attendance_tablets': attendance_tablets, 
    }
    return render(request, "point_of_sales/show.html", context)
@login_required
def point_of_sale_create_view(request):
    form = PointOfSaleForm(request.POST or None)
    if form.is_valid():
        fcc_form = form.save(commit=True)
        return redirect(reverse('store-show', kwargs={'id': fcc_form.store.id}))
    context = {
        'form': form
    }
    return render(request, "point_of_sales/create.html", context)
@login_required
def point_of_sale_update_view(request, id=id):
    obj = get_object_or_404(PointOfSale, id=id)
    form = PointOfSaleForm(request.POST or None, instance=obj)
    if form.is_valid():
        fcc_form = form.save(commit=True)
        return redirect(reverse('store-show', kwargs={'id': fcc_form.store.id}))
    context = {
        'form': form
    }
    return render(request, "point_of_sales/create.html", context)
@login_required
def point_of_sale_delete_view(request, id):
    obj = get_object_or_404(PointOfSale, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect(reverse('store-show', kwargs={'id': obj.store.id}))
    context = {
        "object": obj
    }
    return render(request, "point_of_sales/delete.html", context)