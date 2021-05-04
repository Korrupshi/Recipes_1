from django.urls import reverse, resolve
from django.test import SimpleTestCase
from main.views import home, detail, search


class TestUrls(SimpleTestCase):
        # Test home url
    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

        # Test search url
    def test_search_url_is_resolved(self):
        url = reverse('search')
        print(resolve(url))
        self.assertEquals(resolve(url).func, search)

        # Test detail url
    def test_detail_url_is_resolved(self):
        url = reverse('detail', args=['search'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, detail)
