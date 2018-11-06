from django.db import models

class Updates(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    summary = models.TextField()
    pub_date = models.DateTimeField()
