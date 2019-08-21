from django import forms
from .models import Medical

class MedicalReport(forms.ModelForm):
    class Meta:
        model = Medical
        fields = ['player', 'injury_type' , 'injury_date' , 'injury_comments', 'recovery_date', 'conditioning_notes' ]
        widgets = {
            'player' : forms.Select(attrs={'class' : 'form-control'}),
            'injury_type' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Injury Type'}),
            'injury_date' : forms.DateInput(attrs={'class' : 'form-control'}),
            'injury_comments' : forms.Textarea(attrs={'class' : 'form-control', 'rows': 3 , 'placeholder' : 'Injury Comments'}),
            'recovery_date' : forms.DateInput(attrs={'class' : 'form-control'}),
            'conditioning_notes' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : 3, 'placeholder' : 'Conditioning Notes'}),
            }