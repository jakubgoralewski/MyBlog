from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from blog.models.post import Post
from blog.models.tag import Tag


class LatestEntriesFeed(Feed):
    title = "Posty."
    link = "/sitenews/"
    description = "Ostatnio dodane posty"

    def items(self):
        return Post.objects.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:256]

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('post_detail', kwargs={"slug": item.slug})


# byłem pijany jak to kodziłem bo nie doczytałem ze blog musi mieć feed per kategoria.
# przepraszam za ten kod. poprawie ;)
# "tak był pijany" ~Dawid Wróbel
class DSP2017Feed(Feed):
    title = "Posty DSP2017"
    link = "/dsp2017/feed"
    description = "Ostatnio dodane posty w kategorii DSP2017"

    def items(self):
        dsp_tag = get_object_or_404(Tag, slug="DSP2017")
        posts = dsp_tag.posts_with.all()
        return posts

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:256]

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('post_detail', kwargs={"slug": item.slug})