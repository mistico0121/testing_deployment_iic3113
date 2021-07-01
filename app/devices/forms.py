from django import forms
from .models import Device
from point_of_sales.models import PointOfSale
from import_export.forms import ImportForm, ConfirmImportForm

class CustomImportForm(ImportForm):
    point_of_sale = forms.ModelChoiceField(
        queryset=PointOfSale.objects.all(),
        required=True)
        
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = [
            'name',
            'model_number',
            'brand',
            'os',
            'color',
            'memory',
            'internal_memory',
            'price',
            'sale',
            'point_of_sale'
        ]