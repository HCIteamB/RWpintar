from django.db import models

class umkm(models.Model):
     title = models.CharField(max_length=200)
     descript = models.TextField
     photo_main = models.ImageField(upload_to='photos/%Y%m/%d/')
     photo_1 = models.ImageField(upload_to='photos/%Y%m/%d/')
     photo_2 = models.ImageField(upload_to='photos/%Y%m/%d/', blank=True)
     photo_3 = models.ImageField(upload_to='photos/%Y%m/%d/', blank=True)
     photo_4 = models.ImageField(upload_to='photos/%Y%m/%d/', blank=True)
     def __str__(self):
        return self.title
