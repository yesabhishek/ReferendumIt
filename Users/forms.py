from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

""" Extended the UserCreationForm and added the email column and added the Forgot password logic  """

class UserRegistrationForm(UserCreationForm):
    
    Email = forms.EmailField()
    First_name = forms.CharField()
    last_name = forms.CharField()
    Address = forms.CharField()
    P_no = forms.IntegerField()
    Dob = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'First_name', 'last_name', 'Address', 'P_no', 'Email','Dob',  'password1' , 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    First_name = forms.CharField()
    last_name = forms.CharField()
    Address = forms.CharField()
    P_no = forms.IntegerField()
    Dob = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'email', 'First_name', 'last_name', 'Address', 'P_no','Dob']

