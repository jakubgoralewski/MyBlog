from django import template
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django.template import Context
from blog.models.tag import Tag

register = template.Library()


@register.simple_tag(name='tags')
def render(tags="all", caption=None):
    shelter_tile_template = get_template('tag/templatetag/tags.html')

    if tags == "all":
        tags = Tag.objects.all()

    context = Context({
        "tags": tags,
        "caption": caption
    })

    result = shelter_tile_template.render(context)
    return mark_safe(result)