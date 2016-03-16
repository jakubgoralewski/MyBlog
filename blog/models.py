from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name="Title", max_length=512)
    content = RichTextField(verbose_name="Content")
    author = models.ForeignKey(User)
    slug = models.SlugField(max_length=128, unique=True)

    is_published = models.BooleanField(default=False)

    published_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "\"%s\" %s@%s" % (self.title, self.author, self.created_date.strftime("%d-%m-%Y %H:%m"))