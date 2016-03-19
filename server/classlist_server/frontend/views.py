from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse(render(request, 'index.html'))

def students(request):
    return HttpResponse(render(request, 'students.html'))

def lessons(request):
    return HttpResponse(render(request, 'lessons.html'))

def how_it_works(request):
    return HttpResponse(render(request, 'how_it_works.html'))