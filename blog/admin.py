from django.contrib import admin
from blog.models.post import Post
from blog.models.tag import Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'author', 'created_date')
    list_editable = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}
#admin.site.register(Post, PostAdmin)


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)