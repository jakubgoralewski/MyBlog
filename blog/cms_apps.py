from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class Blog(CMSApp):
    name = _("blog")
    urls = ["blog.urls.post"]

apphook_pool.register(Blog)


class Tags(CMSApp):
    name = _("tag")
    urls = ["blog.urls.tag"]

apphook_pool.register(Tags)
