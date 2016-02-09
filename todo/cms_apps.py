from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class ToDoList(CMSApp):
    name = _("ToDoList")
    urls = ["todo.urls"]

apphook_pool.register(ToDoList)
