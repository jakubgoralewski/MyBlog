from django import template
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django.template import Context

register = template.Library()


@register.simple_tag(name='tags')
def tags(tags):
    shelter_tile_template = get_template('tag/templatetag/tags.html')

    context = Context({
        "tags": tags,
    })

    result = shelter_tile_template.render(context)
    return mark_safe(result)