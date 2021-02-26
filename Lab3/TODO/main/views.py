from django.shortcuts import render
import json

# Create your views here.





def todo_list(request):
    with open('tasks.json') as f:
       tasks = json.load(f)

    context = {
            "data": tasks
                }
    return render(request, 'main/todo_list.html', context=context)


def complited_todo_list(request):
    with open('tasks.json') as f:
        tasks = json.load(f)

    context = {
        "data": tasks
    }
    return render(request, 'main/completed_todo_list.html', context=context)
