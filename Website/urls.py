from django.urls import path
from .views import index, Regular_program

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', index, name='index'),
    path('Program/', Regular_program, name='programs')

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)