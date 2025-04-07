from django.shortcuts import render, redirect
from .models import Image_Container, Second_image, Background_upload, Bible_quote, Service_data, News_catagory
from .forms import YourModelForm, News_upload
from django.http import JsonResponse


# Create your views here.

def index (request):

    Image_data = Image_Container.objects.all()
    Second_Img = Second_image.objects.all()
    Bible_data = Bible_quote.objects.order_by('-id').first()
    previous_bible = Bible_quote.objects.all()


    context = {
        'image' : Image_data,
        'Sec_img' : Second_Img,
        'BibleGenerate' : Bible_data,
        'previous_bible' : previous_bible
    }
    
    return render (request, 'index.html', context=context)

# Define the location of the html file

def Regular_program (request):

    background_regular = Background_upload.objects.all()

    context = {
        'Regular_image' : background_regular
    }

    return render (request, 'Include/Hero_Banner_Include/Regular_program.html', context=context)



def Service_container (request):

    Service_img = Service_data.objects.all()

    context = {
        'Service_img' : Service_img
    }

    return render (request, 'Include/Hero_Banner_Include/Services.html', context=context)



def Donate (request):

    return render (request, 'Include/Hero_Banner_Include/Donate.html')



def upload_Page (request):

    feach_img = Background_upload.objects.all()
    bible_page = YourModelForm (request.POST or None)

    if request.method == 'POST':
        if bible_page.is_valid():

            bible_page.save()
            bible_page = YourModelForm()
            return redirect ('index')

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


def post_News (request):

    background_regular = Background_upload.objects.all()
    data_loop = News_catagory.objects.all()

    context = {
        'Regular_image' : background_regular,
        'data_loop' : data_loop
    }

    return render (request, 'Include/News/DailyNews.html', context=context)


def news_upload_link (request):

    Form_news = News_upload (request.POST, request.FILES or None)

    if request.method == 'POST':
        if Form_news.is_valid():

            Form_news.save()
            print(Form_news)
            Form_news = News_upload()

    context = {
        'form' : Form_news
    }

    return render (request, 'Include/News/News_upload_page.html', context=context)