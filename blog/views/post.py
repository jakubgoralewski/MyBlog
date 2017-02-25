from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from blog.models.post import Post
from blog.models.tag import Tag


def all_posts_index(request):
    return redirect('all_posts_paginated', 1)


def all_posts(request, page_number):
    template_name = "post/all.html"

    posts = Post.objects.all().order_by("-published_date")
    tags = Tag.objects.all()

    paginator = Paginator(posts, 3)

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.page(paginator.num_pages)

    context = {
        'tags': tags,
        'page': page,
        'paginator': paginator,
    }

    return render_to_response(template_name, context, context_instance=RequestContext(request))


def post_detail(request, slug):
    template_name = "post/detail.html"

    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
    }

    return render_to_response(template_name, context, context_instance=RequestContext(request))
