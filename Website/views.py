from django.shortcuts import render, redirect
from .models import Image_Container, Second_image, Background_upload, Bible_quote
from .forms import YourModelForm
from django.http import JsonResponse


# Create your views here.

def index (request):

    Image_data = Image_Container.objects.all()
    Second_Img = Second_image.objects.all()
    Bible_data = Bible_quote.objects.order_by('create')[:1]

    context = {
        'image' : Image_data,
        'Sec_img' : Second_Img,
        'BibleGenerate' : Bible_data
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


def JSON_data_respond (request):

    data_list = list(Bible_quote.objects.values('BibleName', 'MainVerse'))

    context = {
        'data' : data_list
    }

    return JsonResponse (context=context)