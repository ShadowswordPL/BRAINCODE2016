from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse(render(request, 'index.html'))
