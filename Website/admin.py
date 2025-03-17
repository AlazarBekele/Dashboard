from django.contrib import admin
from .models import Image_Container, Second_image, Bible_quote, Background_upload, Service_Container

# Register your models here.

admin.site.register(Image_Container)
admin.site.register(Second_image)
admin.site.register(Bible_quote)
admin.site.register(Background_upload)
admin.site.register(Service_Container)