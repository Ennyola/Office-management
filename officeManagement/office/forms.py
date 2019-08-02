from django import forms
from django.forms import ModelForm
from .models import Staff
from django.contrib.auth.models import User

class StaffForm(ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    username = forms.CharField(max_length = 50)
    age = forms.IntegerField()
    department = forms.CharField(max_length = 30)
    address = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password','age','address','department']
