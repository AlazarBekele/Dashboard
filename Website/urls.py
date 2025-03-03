from django.urls import path
from .views import index, Regular_program, Service, Donate

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', index, name='index'),
    path('Program/', Regular_program, name='programs'),
    path('Service/', Service, name='service'),
    path('Donate', Donate, name='donate')

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)