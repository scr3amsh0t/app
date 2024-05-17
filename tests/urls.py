from django.test import TestCase
from django.urls import reverse

class URLTests(TestCase):
    def test_url_resolves_to_index_view(self):
        url = reverse('index')


    def test_url_resolves_to_contact_view(self):
        url = reverse('contact')


    def test_url_resolves_to_posts_view(self):
        url = reverse('posts')
 

    def test_url_resolves_to_comments_view(self):
        url = reverse('comments')


    def test_url_resolves_to_handler_posts_view(self):
        url = reverse('handler_posts')


    def test_url_resolves_to_handler_comments_view(self):
        url = reverse('handler_comments')


    def test_index_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_contact_view_status_code(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)