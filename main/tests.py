import os
from django.test import TestCase
from .get_posts import zapros, get_posts_count, get_posts
from os import environ
from django import setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
  
setup()


class GetPostsTests(TestCase):
    def test_zapros(self):
        test_data = [{"text": "Тестовый текст"}]
        response_data = zapros(test_data)
        self.assertEqual(response_data, [{'text': 'Тестовый текст', 'result': 0}])
        print(response_data)
        
    def test_get_posts(self):
        screen_name = "no4vick"
        posts_count = 3
        response_data = get_posts(screen_name, posts_count)

    def get_posts_count(self):
        screen_name = "scr3amsh0t"
        respone_data = get_posts_count(screen_name)

    
