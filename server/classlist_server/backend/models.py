from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    imgs_path = models.CharField(max_length=200) # The path to images for this one
