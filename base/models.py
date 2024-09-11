from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField()
    cast = models.CharField(max_length=200)
