from django import forms
from .models import Bible_quote, News_post

class YourModelForm(forms.ModelForm):
    class Meta:

        model = Bible_quote 
        fields = '__all__'
        labels = {'BibleName': '', 'MainVerse' : ''}

        widgets = {

            'BibleName' : forms.TextInput(attrs={
                'class' : 'form-control roboto',
                'placeholder' : 'Bible verse'
            }),

            'MainVerse' : forms.Textarea (attrs={
                'class' : 'form-control roboto_thin',
                'placeholder' : 'Bible qoute'
            })
                
        }



class News_upload (forms.ModelForm):

    model = News_post
    fields = [ 'title', 'Post_items', 'Descrtion', 'category' ]
    lables = { 'title' : '' }

    widgets = {

        'title' : forms.TextInput(attrs={
            'class' : 'form-control roboto'
        }),

        'Post_items' : forms.ClearableFileInput(attrs={
            'class' : 'form-control roboto'
        }),

        'Descrtion' : forms.Textarea(attrs={
            'class' : 'form-control roboto'
        }),

        'category' : forms.TextInput(attrs={
            'class' : 'input-group'
        }),

    }