from django.urls import path

from .views import (
    index, Regular_program,
    Service_container,
    Donate,
    upload_Page,
    post_News,
    news_upload_link,
    Login_check
)

from .views import custom_404

from django.conf import settings
from django.conf.urls.static import static

from .views import JSON_data_respond

from django.conf.urls import handler404
handler404 = custom_404

urlpatterns = [
    
    path('', index, name='index'),
    path('Program/', Regular_program, name='programs'),
    path('Service/', Service_container, name='service'),
    path('Donate', Donate, name='donate'),
    path('upload/', upload_Page, name='upload_page'),
    path('data/', JSON_data_respond, name='JSON_data_respond'),
    path('news/', post_News, name='news'),
    path('newsupload/', news_upload_link, name='news upload'),
    path('login/', Login_check, name='login')

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)