import random
from django.shortcuts import render
from django.http import JsonResponse
from.models import Task
import logging
import json

logger = logging.getLogger('cleartask')

def hello_world(request):
    return JsonResponse({'message': 'Hello, World!'})

def hello_name(request, name):
    return JsonResponse({'message': f'Hello, {name}!'})

def insert_task(request):
    if(request.method == 'POST'):
        try:
            data = json.loads(request.body)
            name = data.get('name')
            description = data.get('description')
            status = data.get('status')
            task = Task(
                id = random.randint(1, 1000000),
                name=name,
                description=description,
                status=status
            )
            task.save()
        except Exception as e:
            logger.error(f'Unexpected error: {e}')
            return JsonResponse({'error': 'Internal server error'}, status=500)        
    return JsonResponse({'message': 'Task inserted!'})