from django.shortcuts import render
from .models import BG_Img


def index (request):

    Background_Picture = BG_Img.objects().all()

    context = {
        'Background' : Background_Picture
    }

    return render (request, 'index.html', context=context)