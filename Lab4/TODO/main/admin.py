from django.contrib import admin

# Register your models here.
from main.models import TodoList, Task

admin.site.register(TodoList)



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['task', 'mark', 'created']
    list_filter = ['created', 'due_on']
