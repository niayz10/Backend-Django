from django.contrib import auth
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from main.serializers import TaskSerializer, TodoListSerializer, TasksSerializer
from main.models import Task, TodoList, CustomUser


# Create your views here.

class MainViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def todo_list(self, request):
        list = TodoList.objects.get(id=1)
        tasks = Task.objects.filter(list=list, mark=False)
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

    def completed_todo_list(self, request, id):
        list = TodoList.objects.get(id=id)
        tasks = Task.objects.filter(id=id, mark=True)
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, id=id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def create(self, request):
        task = Task.objects.create(task=request.data.get('task'), created=request.data.get('created'),
                                   due_on=request.data.get('due_on'),
                                   owner=CustomUser.objects.get(id=request.data.get('owner')),
                                   mark=request.data.get('mark'),
                                   list=TodoList.objects.get(id=request.data.get('list')))
        task.save()
        return Response({}, status=status.HTTP_201_CREATED)

    def update(self, request, id):
        task = Task.objects.get(id=id)
        task.task = request.data.get('task')
        task.created = request.data.get('created')
        task.due_on = request.data.get('due_on')
        task.owner = CustomUser.objects.get(id=request.data.get('owner'))
        task.mark = request.data.get('mark')
        task.list = TodoList.objects.get(id=request.data.get('list'))
        task.save()
        return Response({}, status=status.HTTP_200_OK)

    def destroy(self, request, id):
        task = Task.objects.get(id=id)
        task.delete()
        return Response({}, status=status.HTTP_200_OK)

    def list_of_todos(self, request):
        todos = TodoList.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)

    def create_todo(self, request):
        todo = TodoList.objects.create(name=request.data.get('name'))
        todo.save()
        return Response({}, status=status.HTTP_201_CREATED)

    def delete_todo(self, request, id):
        todo = TodoList.objects.get(id=id)
        todo.delete()
        return Response({}, status=status.HTTP_200_OK)

    def update_todo(self, request, id):
        todo = TodoList.objects.get(id=id)
        todo.name = request.data.get('name')
        todo.save()
        return Response({}, status=status.HTTP_200_OK)

    def retrieve_todo(self, request, id):
        todo = TodoList.objects.get(id=id)
        serializer = TodoListSerializer(todo)
        return Response(serializer.data)
