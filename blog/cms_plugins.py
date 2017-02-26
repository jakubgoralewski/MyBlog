from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from blog.models.tag import Tag


class SiteTagsPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "/tag/templatetag/tags.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(SiteTagsPlugin, self).render(context, instance, placeholder)

        tags = Tag.objects.all()
        context.update({
            'tags': tags,
            'caption': True,
        })

        return context

plugin_pool.register_plugin(SiteTagsPlugin)