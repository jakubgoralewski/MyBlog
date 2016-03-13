from django.shortcuts import render_to_response
from django.template import RequestContext
from todo.models import ToDo


def test(request):
    template_name = "todo.html"

    context = {
        'todos': ToDo.objects.all()
    }

    return render_to_response(template_name, context, context_instance=RequestContext(request))