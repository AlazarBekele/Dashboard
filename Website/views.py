from django.shortcuts import render

# Create your views here.

def index (request):
    
    return render (request, 'index.html')

def Regular_program (request):

    return render (request, 'Include/Hero_Banner_Include/Regular_program.html')