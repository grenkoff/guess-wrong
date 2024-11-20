from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from words.models import RealWord


class StaticViewSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return ['pages:home', 'play:play', 'words:wordlist']

    def location(self, item):
        return reverse(item)


class WordViewSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return RealWord.objects.all()
