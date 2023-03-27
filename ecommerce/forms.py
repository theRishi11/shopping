from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Address




class Registerform(UserCreationForm):
    first_name =forms.CharField( max_length=200, required=True)
    middle_name =forms.CharField( max_length=200, required=False)
    last_name =forms.CharField( max_length=200, required=True)





class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude  = ("user",)