from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="files/") # The path to images for this one

    @property
    def get_all_lessons_num(self):
        return len(Lesson.objects.all())

    @property
    def get_present_lessons_num(self):
        return len(Lesson.objects.filter(students__id=self.id))

class Lesson(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="files/")
    students = models.ManyToManyField(Student)