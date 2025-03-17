from django.urls import path
from .views import index, Regular_program, Service_container, Donate, upload_Page

from django.conf import settings
from django.conf.urls.static import static

from .views import JSON_data_respond

urlpatterns = [
    
    path('', index, name='index'),
    path('Program/', Regular_program, name='programs'),
    path('Service/', Service_container, name='service'),
    path('Donate', Donate, name='donate'),
    path('upload/', upload_Page, name='upload_page'),
    path('data/', JSON_data_respond, name='JSON_data_respond')

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)