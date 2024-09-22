from django.shortcuts import render
from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({'message': 'Hello, World!'})

def hello_name(request, name):
    return JsonResponse({'message': f'Hello, {name}!'})