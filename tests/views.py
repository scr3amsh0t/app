from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpRequest

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Поиск запрещенного контента')

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Поиск запрещенного контента')

    def test_posts_view(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Поиск запрещенного контента')

    def test_comments_view(self):
        response = self.client.get(reverse('comments'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Поиск запрещенного контента')

    def test_handler_posts_view_post_method(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['textInput'] = 'test_input'
        response = handler_posts(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response['Content-Disposition'], 'attachment; filename="posts.txt"')

    def test_handler_comments_view_get_method(self):
        request = HttpRequest()
        request.method = 'GET'
        request.GET['textInput'] = 'test_input'
        response = handler_comments(request)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertIn('result', response.json())

    def test_handler_posts_view_get_method(self):
        response = self.client.get(reverse('handler_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'')

    def test_handler_comments_view_post_method(self):
        response = self.client.post(reverse('handler_comments'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'error': 'Invalid request'})
