from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from mainapp.models import Contact


class UserForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={
        'class': 'forms.control',
    }))

    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'forms.control',
    }))

    mes = forms.CharField(label='Message', widget=forms.Textarea(attrs={
        'class': 'forms.control',
    }))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'mes')
