from django.db import models

# Create your models here.

class Project (models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    date_release = models.DateField()
    link = models.CharField(max_length=1000)