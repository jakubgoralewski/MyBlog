# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=512)),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('is_published', models.BooleanField(default=False)),
                ('published_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=32)),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='Description', null=True)),
                ('slug', models.SlugField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TagsInPostsManager',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('post', models.ForeignKey(to='blog.Post')),
                ('tag', models.ForeignKey(to='blog.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', through='blog.TagsInPostsManager'),
        ),
    ]
