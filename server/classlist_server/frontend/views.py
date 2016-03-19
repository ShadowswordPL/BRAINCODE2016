from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from backend.models import Student, Lesson

def index(request):
    return HttpResponse(render(request, 'index.html'))

def students(request):
    context = {}
    context["students"] = Student.objects.all()

    return HttpResponse(render(request, 'students.html', context))

def lessons(request):
    context = {}
    context["lessons"] = Lesson.objects.all()

    return HttpResponse(render(request, 'lessons.html', context))

def how_it_works(request):
    return HttpResponse(render(request, 'how_it_works.html'))