from django.conf.urls import patterns, url
from blog.rss_feed import LatestEntriesFeed
from blog.views.post import all_posts, all_posts_index, post_detail


urlpatterns = patterns(
    '',
    url(r'^$', all_posts_index, name="all_posts"),
    url(r'^posts/(?P<page_number>\d+)/$', all_posts, name="all_posts_paginated"),
    url(r'^post/(?P<slug>[^/]+)/$', post_detail, name="post_detail"),

    url(r'^latest/feed/$', LatestEntriesFeed()),
)