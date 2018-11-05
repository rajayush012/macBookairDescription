from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='images/')
    spec_sum = models.CharField(max_length=200)
    detail = models.TextField()
