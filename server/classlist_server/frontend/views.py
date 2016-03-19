from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from backend.models import Student, Lesson

def index(request):
    return HttpResponse(render(request, 'index.html'))

def student(request, student_id):
    context = {}
    if(Lesson.objects.filter(id=student_id).count() > 0):
        context["student"] = Student.objects.filter(id=student_id).first()
    else:
        context["student"] = ""
    return HttpResponse(render(request, 'student.html', context))

def students(request):
    context = {}
    context["students"] = Student.objects.all()

    return HttpResponse(render(request, 'students.html', context))

def lesson(request, lesson_id):
    context = {}
    if(Lesson.objects.filter(id=lesson_id).count() > 0):
        context["lesson"] = Lesson.objects.filter(id=lesson_id).first()
    else:
        context["lesson"] = ""
    return HttpResponse(render(request, 'lesson.html', context))

def lessons(request):
    context = {}
    context["lessons"] = Lesson.objects.all()

    return HttpResponse(render(request, 'lessons.html', context))

def how_it_works(request):
    return HttpResponse(render(request, 'how_it_works.html'))