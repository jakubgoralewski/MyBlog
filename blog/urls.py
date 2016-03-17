from django.conf.urls import patterns, url
from blog.views import all_posts_view, post_detail


urlpatterns = patterns('',
    url(r'^$', all_posts_view, name="all_posts"),
    url(r'^post/(?P<slug>[^/]+)/$', post_detail, name="post_detail"),

)