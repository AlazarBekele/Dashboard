from django.shortcuts import render

# Create your views here.

def index (request):
    
    return render (request, 'index.html')

# Define the location of the html file

def Regular_program (request):

    return render (request, 'Include/Hero_Banner_Include/Regular_program.html')

def Service (request):

    return render (request, 'Include/Hero_Banner_Include/Services.html')

def Donate (request):

    return render (request, 'Include/Hero_Banner_Include/Donate.html')