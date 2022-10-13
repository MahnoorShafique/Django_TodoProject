from email.policy import default
from django.contrib import admin


from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    fields = ['task_name', 'status','description','due_date','updated_date','created_date']

admin.site.register(Todo, TodoAdmin)
# admin.site.register(Todo)