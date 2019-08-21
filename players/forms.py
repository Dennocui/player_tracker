from django import forms
from .models import Player, Club, High_school

class NewPlayer(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name' , 'weight' , 'height', 'date_of_birth', 'allergy', 'injury_history', 'email', 'phone_number', 'kin', 'kin_contact', 'position', 'club', 'school', 'tertiary_institution', 'skills', 'about_player', 'image', 'address', 'address_contact', 'id_number']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'First Name'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Last Name'}),
            'weight' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Weight (Kgs)'}),
            'height' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Height (Cm)'}),
            'date_of_birth' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Date Of Birth'}),
            'allergy' : forms.Textarea(attrs={'class' : 'form-control', 'rows': 3, 'placeholder' : 'Allergies'}),
            'injury_history' : forms.Textarea(attrs={'class' : 'form-control', 'rows': 3, 'placeholder' : 'Injury History'}),
            'email' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Email'}),
            'phone_number' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Phone Number'}),
            'kin' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Next Of Kin'}),
            'kin_contact' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Kin Contact'}),
            'position' : forms.Select(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Position'}),
            'club' : forms.Select(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Club'}),
            'school' : forms.Select(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'High School'}),
            'tertiary_institution' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Tertiary Institution'}),
            'skills' : forms.Textarea(attrs={'class' : 'form-control','rows': 3, 'placeholder' : 'Skills'}),
            'about_player' : forms.Textarea(attrs={'class' : 'form-control','rows': 3, 'placeholder' : 'About Player'}),
            'image' : forms.FileInput(attrs={'class' : 'form-control'}),
            'address': forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Address'}),
            'address_contact': forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Address Contact'}),
            'id_number': forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'ID / Passport Number'}),
            
           }

class NewClub(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'coach_name', 'coach_contact', 'team_manager', 'team_manager_contact']
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Enter Club Name'}),
            'coach_name' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Enter Coach Name'}),
            'coach_contact' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Enter Coach Contact'}),
            'team_manager' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Enter Team Manager Name'}),
            'team_manager_contact' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Enter Team Manager Contact'}),
        }


class NewSchool(forms.ModelForm):
    class Meta:
        model = High_school
        fields = ['name', 'location', 'patron', 'patron_contact'] 
        widgets = {
                'name' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Enter School Name'}),
                'location' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Enter School Location'}),
                'patron' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Enter Patron Name'}),
                'patron_contact' : forms.TextInput(attrs={'class' : 'form-control has-feedback-right', 'placeholder' : 'Enter Patron Contact'}),
            }