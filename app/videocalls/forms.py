from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        ratings = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"))
        fields = [
            'quality',
            'usefullness',
            'quality_rating',
            'usefullness_rating'
        ]
        widgets = {
            'quality': forms.Textarea(attrs={'style': 'display: flex; margin-left: 30px;'}),
            'quality_rating': forms.Select(choices=ratings, attrs={'style': 'display: flex; margin-left: 30px;'}),
            'usefullness': forms.Textarea(attrs={'style': 'display: flex; margin-left: 30px;'}),
            'usefullness_rating': forms.Select(choices=ratings, attrs={'style': 'display: flex; margin-left: 30px;'}),
        }
        labels = {
            'quality': ('-------¿Cómo fue la calidad de audio y video durante su videollamada?'),
            'quality_rating': ('-------Evalúe la calidad de la llamada, siendo 1 muy malo y 5 muy bueno'),
            'usefullness': ('-------¿Qué tan útil le fue la ayuda entregada?'),
            'usefullness_rating': ('-------Evalúe la utilidad de la ayuda, siendo 1 muy malo y 5 muy bueno'),
        }