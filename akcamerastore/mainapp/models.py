from django.db import models

# Create your models here.
class Camera(models.Model):
    name = models.TextField()
    desc = models.TextField()
    price = models.CharField(max_length=20)
    accessory = models.BooleanField(default=False)
    carousel = models.BooleanField(default=False)
    img = models.ImageField(upload_to='media')
    img2 = models.ImageField(upload_to='media', blank=True)
    img3 = models.ImageField(upload_to='media', blank=True)
    img4 = models.ImageField(upload_to='media', blank=True)
    img5 = models.ImageField(upload_to='media', blank=True)
    img6 = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.name