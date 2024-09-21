from django.shortcuts import render
from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({'message': 'Hello, World!'})

def hello_world_3(request):
    return JsonResponse({'message': 'Hello, World!'})
