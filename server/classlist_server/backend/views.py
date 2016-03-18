from django.shortcuts import render

from django.http import JsonResponse

def check(request):
    return JsonResponse({'foo':'bar'})
