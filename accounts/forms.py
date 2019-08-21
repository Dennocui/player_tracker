from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
#from .models import Player

class UserRegistrationForm(forms.Form):
	username = forms.CharField(
						label='Username ', 
						max_length=100,
						min_length=5,
						widget=forms.TextInput(attrs={'class' : 'form-control', 'Placeholder' : 'Enter Username'}))
	
	email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control', 'Placeholder' : 'Enter Email'}))
	
	password1 = forms.CharField(
						 label='Password ',
						 max_length=100,
						 min_length=5,
						 widget=forms.PasswordInput(attrs={'class' : 'form-control', 'Placeholder' : 'Enter Password'}))
	password2 = forms.CharField(
						 label='Confirm Password ',
						 max_length=100,
						 min_length=5,
						 widget=forms.PasswordInput(attrs={'class' : 'form-control', 'Placeholder' : 'Enter Password Again'}))

		
	def clean_email(self):
		email = self.cleaned_data['email']
		qs= User.objects.filter(email=email)
		if qs.exists():
			raise ValidationError('Emails is already registred')
		return email

	#def clean_password1(self):
		#this will raise a key error because it refrences password2 field
		#which is ran AFTer password1 validation
	#	p1 = self.cleaned_data['password1']
	#	p2 = self.cleaned_data['password2']
	#	if p1 != p2:
	#		raise ValidationError('Password1 Does Not Match Password2') 
	#	return p1


	#def clean_password2(self):
	#	p1 = self.cleaned_data['password1']
	#	p2 = self.cleaned_data['password2']
	#	if p1 != p2:
	#		raise ValidationError('Password2 Does Not Match Password1') 
	#	return p2

	def clean(self):
		cleaned_data = super().clean()
		p1 = cleaned_data.get('password1')
		p2 = cleaned_data.get('password2')

		if p1 and p2:
			if p1 != p2:
				raise ValidationError('Passwords Do ot Match')