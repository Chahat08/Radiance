from django.contrib import admin
from .models import Post, Comments, Like, TaskList

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Like)
admin.site.register(TaskList)
'''class TaskListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")

admin.site.register(TaskList, TaskListAdmin)'''