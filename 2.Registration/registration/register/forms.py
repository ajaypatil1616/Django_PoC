from django import forms
from django.forms import EmailField, CharField, IntegerField

gender_choice = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length= 30, required=True)
    last_name = forms.CharField(max_length= 30, required= True)
    age = forms.IntegerField(required=True)
    email = forms.EmailField(max_length= 100, required= True,)
    password = forms.CharField(min_length= 8, required= True,widget=forms.PasswordInput)
    confirm_password = forms.CharField(required=True,widget=forms.PasswordInput)
    number = forms.CharField(min_length=10, max_length=10, required= True)
    
    gender = forms.ChoiceField(choices  =gender_choice)
    dob = forms.DateField()
    # file = forms.FileField(required=True)

    