
from django.conf.urls.defaults import *

from djog import site
from djog.feeds import *

site.add_feed('latest', EntryFeed)
site.add_feed('comments', CommentsByEntryFeed)
site.add_feed('tags', EntriesByTagFeed)
site.add_feed('search', SearchFeed)

urlpatterns = patterns('',
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$',
        site.post, {}, 'djog_post'),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',
        site.archive_day, {}, 'djog_archive_daily'),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
        site.archive_month, {}, 'djog_archive_month'),
    (r'^(?P<year>\d{4})/$',
        site.archive_year, {}, 'djog_archive_year'),
    (r'^tags/(?P<slug>[-\w]+)/$',
        site.entries_by_tag, {}, 'djog_entries_by_tag'),
    (r'^feeds/(?P<url>.*)/$',
        site.feed, {}, 'djog_feed'),
    (r'^search/$',
        site.search, {}, 'djog_search'),
    (r'^trackback/(?P<id>\d+)/$',
        site.trackback, {}, 'djog_trackback'),
    (r'^(?P<slug>[-\w]+)/$',
        site.page, {}, 'djog_page'),
    (r'^$',
        site.archive_index, {}, 'djog_index'),
)

# TODO: fix these
urlpatterns += patterns('',
    (r'^comments/', include('django.contrib.comments.urls.comments')),
)
