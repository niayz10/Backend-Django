from django.urls import path
from .views import *


urlpatterns = [
    path('todos', todo_list, name='todo_list'),
    path('todos/1/completed', complited_todo_list, name='complited_todo_list'),

]