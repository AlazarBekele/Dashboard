from django import forms
from .models import *

class YourModelForm(forms.ModelForm):
    class Meta:

        model = Bible_random 
        fields = '__all__'

    widgets = {

        'Bible_name' : forms.TextInput (attrs={
            'class' : 'form-control',
            'type' : 'text'
        }),

        'Main_verse' : forms.Textarea (attrs={
            'class' : 'form-control'
        })

    }