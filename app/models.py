from distutils.command.upload import upload
from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    cars_image = models.ImageField(upload_to='cars_image')
    file = models.FileField(upload_to='files')
    year = models.IntegerField()

    def __str__(self):
        return self.name