from django import template
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django.template import Context

register = template.Library()


@register.simple_tag(name='post_miniature')
def post_miniature(post):
    shelter_tile_template = get_template('post/templatetag/miniature.html')

    context = Context({
        "post": post,
    })

    result = shelter_tile_template.render(context)
    return mark_safe(result)