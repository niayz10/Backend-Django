from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from main.views import MainViewSet


urlpatterns = [
    path('login', obtain_jwt_token),
    path('todos', MainViewSet.as_view({'get': 'todo_list', 'post': 'create'})),
    path('todos/<int:id>/completed', MainViewSet.as_view({'get': 'completed_todo_list'})),
    path('todo/<int:id>', MainViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('listoftodo', MainViewSet.as_view({'get': 'list_of_todos', 'post': 'create_todo'})),
    path('listoftodo/<int:id>', MainViewSet.as_view({'get': 'retrieve_todo', 'delete': 'delete_todo',
                                                     'put': 'update_todo', }))
]

