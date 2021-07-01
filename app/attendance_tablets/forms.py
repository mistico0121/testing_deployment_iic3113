from django import forms
from .models import AttendanceTablet

class AttendanceTabletForm(forms.ModelForm):
    class Meta:
        model = AttendanceTablet
        fields = [
            'name',
            'online',
            'point_of_sale'
        ]