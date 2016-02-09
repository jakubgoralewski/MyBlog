from django.shortcuts import render_to_response
from django.template import RequestContext


def test(request):
    template_name = "todo.html"

    context = {'test': "test2"}

    return render_to_response(template_name, context, context_instance=RequestContext(request))