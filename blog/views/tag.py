from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models.post import Post
from blog.models.tag import Tag


def all_posts_with_tag(request, tag):
    template_name = "tag/all_with_tag.html"

    posts = Post.objects.all()


    context = {
        'tag': get_object_or_404(Tag, name=tag),
        'posts': posts
    }

    return render_to_response(template_name, context, context_instance=RequestContext(request))
