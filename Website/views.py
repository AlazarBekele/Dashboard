from django.shortcuts import render, redirect
from .models import Image_Container, Second_image, Background_upload
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

    background_regular = Background_upload.objects.all()

    context = {
        'Regular_image' : background_regular
    }

    return render (request, 'Include/Hero_Banner_Include/Regular_program.html', context=context)

def Service (request):

    return render (request, 'Include/Hero_Banner_Include/Services.html')

def Donate (request):

    return render (request, 'Include/Hero_Banner_Include/Donate.html')

def upload_Page (request):

    feach_img = Background_upload.objects.all()
    bible_page = YourModelForm (request.POST or None)

    if request.method == 'POST':
        if bible_page.is_valid():

            bible_page.save()

    context = {
        'form' : bible_page,
        'feach' : feach_img
    }


    return render (request, 'Upload_bible.html', context=context)