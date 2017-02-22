from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models.post import Post, TagsInPostsManager
from blog.models.tag import Tag


def all_tags(request):
    template_name = "tag/all.html"

    tags = Tag.objects.all()

    context = {
        'tags': tags,
    }

    return render_to_response(template_name, context, context_instance=RequestContext(request))


def all_posts_with_tag(request, slug):
    template_name = "tag/posts_with_tag.html"

    tag = get_object_or_404(Tag, slug=slug)
    posts = tag.posts_with.all()
    tags = Tag.objects.all()

    context = {
        'tag': tag,
        'tags': tags,
        'posts': posts
    }

    return render_to_response(template_name, context, context_instance=RequestContext(request))
