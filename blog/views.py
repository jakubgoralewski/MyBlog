from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Post


def all_posts_view(request):
    template_name = "all_posts.html"

    context = {
        'posts': Post.objects.all()
    }

    return render_to_response(template_name, context, context_instance=RequestContext(request))