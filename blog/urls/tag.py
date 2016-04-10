from django.conf.urls import patterns, url
from blog.views.tag import all_tags, all_posts_with_tag


urlpatterns = patterns(
    '',
    url(r'^$', all_tags, name="all_tags"),
    url(r'^tag/(?P<slug>[^/]+)/$', all_posts_with_tag, name="post_with_tag"),
)