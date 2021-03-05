from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=200)


class Task(models.Model):
    task = models.CharField(max_length=200)
    created = models.DateField()
    due_on = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.BooleanField(default=False)
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
