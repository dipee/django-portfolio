from django.forms import ModelForm
from django import forms
from .models import Contact

class ContactModelForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'email': forms.EmailInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea mt-1 block w-full'}),
        }