from django.contrib import admin
from blog.models.post import Post, TagsInPostsManager
from blog.models.tag import Tag


class TagInline(admin.TabularInline):
    model = TagsInPostsManager
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'author', 'created_date')
    list_editable = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = (TagInline,)



@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}