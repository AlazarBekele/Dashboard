from django import forms
from .models import Bible_quote, News_post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        fields = [ 'title', 'Post_img', 'Descrption', 'category' ]
        labels = {
            'title': '',
            'Descrption' : '',
            'category' : '',
            'Post_img' : ''
        }

        widgets = {

            'title' : forms.TextInput(attrs={
                'class' : 'form-control roboto',
                'placeholder' : 'Enter Title'
            }),

            'Post_img' : forms.ClearableFileInput (attrs={
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

class Login_data (UserCreationForm):

    First_Name = forms.CharField (max_length=20 , widget = forms.TextInput(attrs={

        'class' : 'Name_container',
        'placeholder' : 'First Name',
        'autocomplate' : 'off'

    }))

    Last_Name = forms.CharField (max_length=20 , widget = forms.TextInput(attrs={

        'class' : 'Name_container',
        'placeholder' : 'First Name',
        'autocomplate' : 'off'

    }))

    User_Name = forms.CharField (max_length=8 , widget = forms.TextInput(attrs={

        'class' : 'Name_container',
        'placeholder' : 'First Name',
        'autocomplate' : 'off'

    }))

    Password = forms.CharField  (max_length=8, label='Password', widget = forms.PasswordInput(attrs={

        'class' : 'Name_container',
        'placeholder' : 'Password',
        'autocomplate' : 'off'

    }))

    Password_cconfirm = forms.CharField  (max_length=8, label='Password confirm', widget = forms.PasswordInput(attrs={

        'class' : 'Name_container',
        'placeholder' : 'Password confirm',
        'autocomplate' : 'off'

    }))

    class Meta:
        
        model = User
        fields = ('First_Name', 'Last_Name', 'User_Name', 'Password', 'Password_cconfirm')