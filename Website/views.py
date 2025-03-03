from django.shortcuts import render
from .models import Image_Container


# Create your views here.

def index (request):

    Image_data = Image_Container.objects.all()

    context = {
        'image' : Image_data
    }
    
    return render (request, 'index.html', context=context)

# Define the location of the html file

def Regular_program (request):

    return render (request, 'Include/Hero_Banner_Include/Regular_program.html')

def Service (request):

    return render (request, 'Include/Hero_Banner_Include/Services.html')

def Donate (request):

    return render (request, 'Include/Hero_Banner_Include/Donate.html')