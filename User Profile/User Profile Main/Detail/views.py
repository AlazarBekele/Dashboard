from django.shortcuts import render
from .models import Detail_Background_Img

def index (request):

    Background_Data = Detail_Background_Img.objects.all()

    context = {

        'Img' : Background_Data

    }

    return render (request, 'index.html', context=context)