from django.contrib import admin
from .models import Post, Comments, Like, TodoList, Category

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Like)

class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(TodoList, TodoListAdmin)
admin.site.register(Category, CategoryAdmin)