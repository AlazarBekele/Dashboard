from django.shortcuts import render, redirect
from .models import Image_Container, Second_image
from .forms import YourModelForm


# Create your views here.

def index (request):

    Image_data = Image_Container.objects.all()
    Second_Img = Second_image.objects.all()

    context = {
        'image' : Image_data,
        'Sec_img' : Second_Img
    }
    
    return render (request, 'index.html', context=context)

# Define the location of the html file

def Regular_program (request):

    return render (request, 'Include/Hero_Banner_Include/Regular_program.html')

def Service (request):

    return render (request, 'Include/Hero_Banner_Include/Services.html')

def Donate (request):

    return render (request, 'Include/Hero_Banner_Include/Donate.html')

def upload_Page (request):

    bible_page = YourModelForm (request.POST or None)

    if request.method == 'POST':
        if bible_page.is_valid():

            bible_page.save()
            

    context = {
        'form' : bible_page
    }


    return render (request, 'Upload_bible.html', context=context)