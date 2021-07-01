from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import AttendanceTablet
from .forms import AttendanceTabletForm
from django.contrib.auth.decorators import login_required

@login_required
def attendance_tablet_index_view(request):
    queryset = AttendanceTablet.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "attendance_tablet/index.html", context)
@login_required
def attendance_tablet_show_view(request, id=id):
    obj = get_object_or_404(AttendanceTablet, id=id)
    context = {
        'object': obj
    }
    return render(request, "attendance_tablet/show.html", context)
@login_required
def attendance_tablet_create_view(request):
    form = AttendanceTabletForm(request.POST or None)
    if form.is_valid():
        fcc_form = form.save(commit=True)
        return redirect(reverse('point_of_sale-show', kwargs={'id': fcc_form.point_of_sale.id}))
    context = {
        'form': form
    }
    return render(request, "attendance_tablet/create.html", context)
@login_required
def attendance_tablet_update_view(request, id=id):
    obj = get_object_or_404(AttendanceTablet, id=id)
    form = AttendanceTabletForm(request.POST or None, instance=obj)
    if form.is_valid():
        fcc_form = form.save(commit=True)
        return redirect(reverse('point_of_sale-show', kwargs={'id': fcc_form.point_of_sale.id}))
    context = {
        'form': form
    }
    return render(request, "attendance_tablet/create.html", context)
@login_required
def attendance_tablet_delete_view(request, id):
    obj = get_object_or_404(AttendanceTablet, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect(reverse('point_of_sale-show', kwargs={'id': obj.point_of_sale.id}))
    context = {
        "object": obj
    }
    return render(request, "attendance_tablet/delete.html", context)