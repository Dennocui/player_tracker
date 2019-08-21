from django import forms
from .models import Condition


class ConditioningReport(forms.ModelForm):
	class Meta:
		model = Condition
		fields = ['player', 'bench' , 'squats' , 'v_jumps', 'h_jumps', 'yoyo', 't_test_right', 't_test_left', 'chest', 'bicep', 'waist', 'hip', 'thigh', 'm10', 'm40', 'm60', 'suppliment_taken', 'conditioning_notes']
		widgets = {
			'player' : forms.Select(attrs={'class' : 'form-control ', 'min' : '0', 'value' : '0', 'step' : '01'}),
			'bench' : forms.TextInput(attrs={'class' : 'form-control ', 'min' : '0', 'value' : '0', 'step' : '01'}),
			'squats' : forms.TextInput(attrs={'class' : 'form-control ', 'min' : '0', 'value' : '0', 'step' : '01'}),
			'v_jumps' : forms.TextInput(attrs={'class' : 'form-control ', 'min' : '0', 'value' : '0', 'step' : '01'}),
			'h_jumps' : forms.TextInput(attrs={'class' : 'form-control ', 'min' : '0', 'value' : '0', 'step' : '01'}),
			'yoyo' : forms.TextInput(attrs={'class' : 'form-control ', 'min' : '0', 'value' : '0', 'step' : '01'}),
			't_test_right' : forms.TextInput(attrs={'class' : 'form-control ', 'min' : '0', 'value' : '0', 'step' : '01'}),
			't_test_left' : forms.TextInput(attrs={'class' : 'form-control ', 'min' : '0', 'value' : '0', 'step' : '01'}),
			'chest' : forms.TextInput(attrs={'class' : 'form-control', 'min' : '0', 'value' : '0', 'step' : '01'}),
			'bicep' : forms.TextInput(attrs={'class' : 'form-control', 'min' : '0', 'value' : '0', 'step' : '01'}),
			'waist' : forms.TextInput(attrs={'class' : 'form-control', 'min' : '0', 'value' : '0', 'step' : '01'}),
			'hip' : forms.TextInput(attrs={'class' : 'form-control', 'min' : '0', 'value' : '0', 'step' : '01'}),
			'thigh' : forms.TextInput(attrs={'class' : 'form-control', 'min' : '0', 'value' : '0', 'step' : '01'}),
			'm10' : forms.TextInput(attrs={'class' : 'form-control', 'min' : '0', 'value' : '0', 'step' : '01'}),
			'm40' : forms.TextInput(attrs={'class' : 'form-control', 'min' : '0', 'value' : '0', 'step' : '01'}),
			'm60' : forms.TextInput(attrs={'class' : 'form-control', 'min' : '0', 'value' : '0', 'step' : '01'}),
			'suppliment_taken' : forms.Textarea(attrs={'class' : 'form-control', 'rows': 3 , 'placeholder' : 'Suppliment Taken'}),
			'conditioning_notes' : forms.Textarea(attrs={'class' : 'form-control', 'rows': 3 , 'placeholder' : 'Conditioning Notes'}),
			}

																    