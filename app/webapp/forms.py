from django import forms
from django.forms import ModelForm

from .models import *

class ThreadForm(forms.ModelForm):
	class Meta:
		model = Thread
		fields = '__all__'