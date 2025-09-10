from django.contrib import admin
from .models import Blogs, Category, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'updated_at', 'created_at')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'category', 'author', 'is_featured', 'status', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('id', 'title', 'author__username')
    list_filter = ('category', 'status', 'author')
    list_editable = ('is_featured', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blogs, BlogAdmin)
admin.site.register(Comment)