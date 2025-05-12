from django import forms
from .models import Enroll

class EnrollForm(forms.ModelForm):
    class Meta:
        model = Enroll
        fields = ['firstname', 'lastname', 'gender', 'dob', 'address', 'state', 'telephone', 'email', 'passport', 'enroll_date'] 
