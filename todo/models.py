from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class ToDo(models.Model):
    title = models.CharField(verbose_name="ToDo Title", max_length=512)
    note = RichTextField()
    author = models.ForeignKey(User)

    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<%s> '%s' at: %s" % (self.title, self.author, self.created_date)

