from django.db import models

# Create your models here.

class BG_Img (models.Model):
  
  Name = models.CharField (max_length=20)
  Image = models.ImageField (upload_to='photo/')

  def __str__(self):
    return self.Name