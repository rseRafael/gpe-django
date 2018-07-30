from django.db import models


class FileMetaDate(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField()
    
# Create your models here.
