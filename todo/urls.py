from django.conf.urls import patterns, url
from todo.views import test


urlpatterns = patterns('',
    url(r'^$', test, name="test"),
    url(r'test^$', test, name="test2"),
)