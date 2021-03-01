from django.db import models

# Create your models here.

class EatModel(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    author = models.CharField(max_length=20)
    snsimage = models.ImageField(upload_to='media/')
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.TextField(null=True, blank=True, default='a')
    subtitle = models.TextField(null=True, blank=True, default='a')
    material = models.TextField(null=True, blank=True, default='a')