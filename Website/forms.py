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
    class Meta:

        model = News_post
        fields = [ 'title', 'Post_items', 'Descrption', 'category' ]
        labels = {
            'title': '',
            'Post_items' : '',
            'Descrption' : '',
            'category' : ''
        }

        widgets = {

            'title' : forms.TextInput(attrs={
                'class' : 'form-control roboto',
                'placeholder' : 'Enter Title'
            }),

            'Post_items' : forms.ClearableFileInput(attrs={
                'class' : 'form-control roboto',
            }),

            'Descrption' : forms.Textarea(attrs={
                'class' : 'form-control roboto',
                'placeholder' : 'What in your mind?'
            }),

            'category' : forms.Select(attrs={
                'class' : 'form-control roboto',
            }),

        }