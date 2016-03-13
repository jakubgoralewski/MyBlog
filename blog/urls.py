from django.conf.urls import patterns, url
from blog.views import all_posts_view


urlpatterns = patterns('',
    url(r'^$', all_posts_view, name="all_posts"),

)