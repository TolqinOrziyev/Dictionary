from django.db import models


# Create your models here.
class Dictionary(models.Model):
    inglizcha = models.CharField('Inglizcha', max_length=100)
    ozbekcha = models.CharField('Ozbekcha', max_length=100)