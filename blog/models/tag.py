from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from django.db import models

__author__ = 'Jakub'


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="Name")
    description = RichTextField(blank=True, null=True, verbose_name="Description")
    slug = models.SlugField(max_length=128, unique=True)

    def get_absolute_url(self):
        return reverse('bolg.views.tag.all_posts_with_tag', args=[str(self.slug)])

    def __str__(self):
        return self.name


