from django import forms
from .models import Bible_quote

class YourModelForm(forms.ModelForm):
    class Meta:

        model = Bible_quote 
        fields = '__all__'

    widgets = {

        'BibleName' : forms.TextInput(attrs={
            'class' : 'form-control',
        }),

        'MainVerse' : forms.Textarea (attrs={
            'class' : 'form-control',
        })
            
    }