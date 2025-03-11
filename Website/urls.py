from django.urls import path
from .views import index, Regular_program, Service, Donate, upload_Page

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', index, name='index'),
    path('Program/', Regular_program, name='programs'),
    path('Service/', Service, name='service'),
    path('Donate', Donate, name='donate'),
    path('upload/', upload_Page, name='upload_page')

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)