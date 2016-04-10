from django.conf.urls import patterns, url

from blog.views.post import all_posts_view, post_detail
from blog.views.tag import all_posts_with_tag


urlpatterns = patterns(
    '',
    url(r'^$', all_posts_view, name="all_posts"),
    url(r'^post/(?P<slug>[^/]+)/$', post_detail, name="post_detail"),
)