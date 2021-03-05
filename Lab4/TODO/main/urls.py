from django.urls import path
from .views import *


urlpatterns = [
    path('todos', todo_list),
    path('todos/<int:id>/completed', complited_todo_list),
]