from django.db import models

__author__ = 'Jakub'


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="Name")

    def __str__(self):
        return "Tag: %s" % self.name


