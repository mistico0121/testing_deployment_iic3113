from django.contrib import admin
from .models import Device
from import_export.admin import ImportMixin
from import_export import resources
from .forms import CustomImportForm
from import_export.formats import base_formats

class DeviceResource(resources.ModelResource):

    def __init__(self, request=None):
        super(DeviceResource, self).__init__()
        self.request = request

    

    def before_import_row(self, row, **kwargs):
        point_of_sale = self.request.POST.get('point_of_sale', None)
        if point_of_sale:
            self.request.session['import_context_point_of_sale'] = point_of_sale
        else:
            # If this raises a KeyError we want to know about it. It means that we got to a point of importing data
            #   without company context, and we do not want to continue.
            try:
                point_of_sale = self.request.session['import_context_point_of_sale']
            except KeyError as e:
                raise Exception(f'Point Of Sale context failure on row import, check resources.py for more info: {e}')
        row['point_of_sale'] = point_of_sale

    class Meta:
        model = Device
    

class DeviceAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = DeviceResource

    def get_import_form(self):
        return CustomImportForm

    def get_resource_kwargs(self, request, *args, **kwargs):
        rk = super().get_resource_kwargs(request, *args, **kwargs)
        rk['request'] = request
        return rk

    def get_import_formats(self):
        formats = (
            base_formats.CSV,
        )

        return [f for f in formats if f().can_export()]
    

admin.site.register(Device, DeviceAdmin)