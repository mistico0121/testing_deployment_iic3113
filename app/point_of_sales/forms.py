from django import forms
from .models import PointOfSale

class PointOfSaleForm(forms.ModelForm):
    class Meta:
        model = PointOfSale
        fields = [
            'name',
            'description',
            'store',
        ]