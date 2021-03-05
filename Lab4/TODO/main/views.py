from django.shortcuts import render


# Create your views here.
from main.models import TodoList, Task


def todo_list(request):
    list = TodoList.objects.get(id=1)
    tasks = Task.objects.filter(list=list, mark=False)
    context = {
        'tasks': tasks
    }
    return render(request, 'main/todo_list.html', context=context)


def complited_todo_list(request, id):
    list = TodoList.objects.get(id=id)
    tasks = Task.objects.filter(list=list, mark=True)
    context = {
        'tasks': tasks
    }

    return render(request, 'main/completed_todo_list.html', context=context)