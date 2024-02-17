from django.contrib import admin
from todoapp.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    pass
#list_display = ['eno','ename','esalary']
admin.site.register(Task,TaskAdmin)