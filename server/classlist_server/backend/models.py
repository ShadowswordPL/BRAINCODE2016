from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="files/")
    msFaceId = models.CharField(max_length=250) # This expires every 24 hours
    # But it's a hackathon so we don't really give a fuck :).

    @property
    def get_all_lessons_num(self):
        return len(Lesson.objects.all())

    @property
    def get_absent_lessons(self):
        toReturn = ""
        for lesson in Lesson.objects.exclude(students__id=self.id):
            toReturn += str(lesson)  + "<br>"
        if toReturn == "":
            return "This student was present at every lesson"
        return toReturn

    @property
    def get_present_lessons_num(self):
        return len(Lesson.objects.filter(students__id=self.id))

    @property
    def get_present_lessons(self):
        toReturn = ""
        for lesson in Lesson.objects.filter(students__id=self.id):
            toReturn += str(lesson) + "<br>"
        if toReturn == "":
            return "This student was absent at every lesson"
        return toReturn

class Lesson(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="files/")
    students = models.ManyToManyField(Student)
    dateTime = models.DateTimeField(auto_now_add=True)

    @property
    def get_present_students_num(self):
        return len(self.students.all())

    @property
    def get_absent_students_num(self):
        return len(Student.objects.all()) - len(self.students.all())

    @property
    def my_str(self):
        return str(self)

    def __str__(self):
        return "<a href='#'>" + str(self.name) + '</a>'