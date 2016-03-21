from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models.post import Post


def all_posts_view(request):
    template_name = "post/all.html"

    context = {
        'posts': Post.objects.all()
    }

    return render_to_response(template_name, context, context_instance=RequestContext(request))


def post_detail(request, slug):
    template_name = "post/detail.html"

    context = {
        'post': get_object_or_404(Post, slug=slug)
    }

    return render_to_response(template_name, context, context_instance=RequestContext(request))
