from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from blog.models.tag import Tag

__author__ = "Jakub"


class Post(models.Model):
    title = models.CharField(max_length=512, verbose_name="Title")
    content = RichTextField(verbose_name="Content")
    author = models.ForeignKey(User)
    slug = models.SlugField(max_length=128, unique=True)

    is_published = models.BooleanField(default=False)

    published_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(Tag, through='TagsInPostsManager')

    def get_absolute_url(self):
        return reverse('bolg.views.post_detail', args=[str(self.slug)])

    def __str__(self):
        return "\"%s\" %s@%s" % (self.title, self.author, self.created_date.strftime("%d-%m-%Y %H:%m"))


class TagsInPostsManager(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


