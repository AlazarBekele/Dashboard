from django.db import models

# Create your models here.

class Image_Container (models.Model):

    image_name = models.CharField (max_length=20)
    # picture = models.ImageField (upload_to='photo/')

    def __str__(self):
        return self.image_name
    

class Second_image (models.Model):

    Second_img = models.CharField (max_length=20)
    # Second_picture = models.ImageField (upload_to='photo/')

    def __str__(self):
        return self.Second_img