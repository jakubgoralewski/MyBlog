# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Description', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(unique=True, max_length=128, default=''),
        ),
    ]
