from django.db import models

# Create your models here.
class Specs(models.Model):
    basis = models.CharField(max_length=50)
    specifics = models.TextField()
