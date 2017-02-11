from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blog.models.post import Post


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