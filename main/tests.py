from django.test import TestCase, Client
from django.http import HttpRequest
from django.urls import reverse
import unittest
from unittest.mock import patch
from .main import get_name, get_screen_name
from . import views
from django.urls import reverse
from .get_posts import get_posts_count, zapros


class SimpleTest(TestCase):
    def test_posts_reverse(self):
        url = reverse('posts')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_posts_count(self):
        screen_name = "scr3amsh0t"
        response = get_posts_count(screen_name)

    def test_zapros(self):
        test_data = [{"text":"Тестовые данные"}]
        response_data = zapros(test_data)
        self.assertEquals(response_data, [{"text":"Тестовые данные", 'result': 0}])
        print(response_data)


    def test_get_name_incorrect_url(self):
        url = 'https://incorrect.com/someuser'
        with self.assertRaises(SystemExit):
            get_name(url)

    @patch('main.requests.get')
    def test_get_screen_name(self, mock_get):
        mock_response = {
            'response': {
                'object_id': 12345,
                'type': 'user'
            }
        }
        mock_get.return_value.json.return_value = mock_response

        name = 'someuser'
        screen_name = get_screen_name(name)
        self.assertEqual(screen_name, 12345)

        mock_response['response']['type'] = 'group'
        screen_name = get_screen_name(name)
        self.assertEqual(screen_name, -12345)


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


    def test_handler_posts_view_get_method(self):
        response = self.client.get(reverse('handler_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'')

    def test_handler_comments_view_post_method(self):
        response = self.client.post(reverse('handler_comments'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'error': 'Invalid request'})