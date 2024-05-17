import unittest
from unittest.mock import patch
from .main import get_name, get_screen_name
from urllib.parse import urlparse
import sys

class TestURLFunctions(unittest.TestCase):

    def test_get_name_correct_url(self):
        url = 'https://vk.com/someuser'
        self.assertEqual(get_name(url), 'someuser')

    def test_get_name_incorrect_url(self):
        url = 'https://incorrect.com/someuser'
        with self.assertRaises(SystemExit):
            get_name(url)

    @patch('main.requests.get')
    def test_get_screen_name(self, mock_get):
        # Мокаем ответ от API
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

        # Тест для не пользователя
        mock_response['response']['type'] = 'group'
        screen_name = get_screen_name(name)
        self.assertEqual(screen_name, -12345)

if __name__ == '__main__':
    unittest.main()
