from django import forms
from .models import Athlete


class AthleteForm(forms.ModelForm):

    class Meta:
        model = Athlete
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date',
                }
            ),
            'description': forms.Textarea,
        }