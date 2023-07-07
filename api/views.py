from django.http import HttpRequest, JsonResponse
from api.models import Task
import json


def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks_json = [task.to_json() for task in tasks]
        return JsonResponse(tasks_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        task = Task.objects.create(
            title=data.get('title'), 
            description=data.get('description'), 
            status=data.get('status')
        )
        return JsonResponse(task.to_json())


def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    
    if request.method == 'GET':
        return JsonResponse(task.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.status = data.get('status', task.status)
        task.save()
        return JsonResponse(task.to_json())
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'deleted': True}, safe=False)