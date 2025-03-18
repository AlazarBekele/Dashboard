from django.db import models

# Create your models here.

class Image_Container (models.Model):

    image_name = models.CharField (max_length=20)
    picture = models.ImageField (upload_to='photo/')

    def __str__(self):
        return self.image_name
    

class Second_image (models.Model):

    Second_img = models.CharField (max_length=20)
    Second_picture = models.ImageField (upload_to='photo/')

    def __str__(self):
        return self.Second_img
    

class Bible_quote (models.Model):

    BibleName = models.CharField (max_length=30)
    MainVerse = models.TextField ()
    create = models.DateField (auto_created=True, auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.BibleName
    
class Background_upload (models.Model):

    Name = models.CharField (max_length=20)
    Image_main = models.ImageField (upload_to='photo/', null=True, blank=True)

    def __str__(self):
        return self.Name
    

class Service_Container_img (models.Model):

    Name = models.CharField (max_length=20)
    Picture = models.ImageField (upload_to='photo/Service')

    def __str__(self):
        return self.Name