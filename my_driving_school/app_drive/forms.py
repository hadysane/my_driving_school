from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from app_drive.models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class CreateRDVForm(forms.ModelForm): 
    class Meta:
        model = RdvDrive
        fields =['place', 'date', 'start_time','end_time',
        'nb_hour','student','instructor']
