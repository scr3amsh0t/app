import csv
import requests
import sys
from urllib.parse import urlparse


def get_name(url):
    parsed_url = urlparse(url)
    if (parsed_url.netloc != 'vk.com'):
        print("Неверная ссылка")                        # проверить другие варианты неверного ввода
        sys.exit()
    else:
        name = parsed_url.path[1:]
        return name



def get_screen_name(name):
    token = 'vk1.a.byMJTaFR8uzQ2VOgF72GpGczOd0RnOu1YBVklpdL9Rnndd-5TSH1FGz94XMiFgw4b13TFUQNikYHk79VQ5jwJ7GHKIoVZb3No7t97wJZTlgj5iqirPrXCXikDQOuSewYbYUbwuMb7kth4YqsAC8pDxBE-ax68I0qYiEHhkFnumJo3HzsWxRgvfPKwMck6jl1IDxVnpZ_uTGQMAZa2Kl9Xg'
    version = 5.199
    response = requests.get('https://api.vk.com/method/utils.resolveScreenName',
                            params={
                                'access_token': token,
                                'v': version,
                                'screen_name': name
                            })

    screen_name = response.json()['response']['object_id']
    type = response.json()['response']['type']
    if type == 'user':
        screen_name = screen_name
    else:
        screen_name = -screen_name
    return screen_name

