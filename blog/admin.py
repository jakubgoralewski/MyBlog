from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'author', 'created_date')
    list_editable = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
