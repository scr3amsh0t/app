import requests
import sys
from urllib.parse import urlparse
from main.main import get_name, get_screen_name

def get_name(url):
    parsed_url = urlparse(url)
    if (parsed_url.netloc != 'vk.com'):
        print("Неверная ссылка")                        # проверить другие варианты неверного ввода
        sys.exit()
    else:
        name = parsed_url.path[1:]
        print(name)
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
    print(response.json())
    screen_name = response.json()['response']['object_id']
    type = response.json()['response']['type']
    if type == 'user':
        screen_name = screen_name
    else:
        screen_name = -screen_name
    return screen_name

def get_account_info(screen_name):
    token = 'vk1.a.byMJTaFR8uzQ2VOgF72GpGczOd0RnOu1YBVklpdL9Rnndd-5TSH1FGz94XMiFgw4b13TFUQNikYHk79VQ5jwJ7GHKIoVZb3No7t97wJZTlgj5iqirPrXCXikDQOuSewYbYUbwuMb7kth4YqsAC8pDxBE-ax68I0qYiEHhkFnumJo3HzsWxRgvfPKwMck6jl1IDxVnpZ_uTGQMAZa2Kl9Xg'
    version = 5.199
    user_id = screen_name
    response = requests.get('https://api.vk.com/method/users.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'user_ids': user_id,
                                'fields': 'is_closed, status, deactivated'
                            })
    data = response.json()['response']
    for info in data:
        data = [info['first_name'], info['last_name'], info['status'], info['is_closed']]
    return data


def file_writer_account(data):                                               
    with open('account_info.txt', 'w', newline='', encoding="utf-8") as file:
        file.write("%s\n" % data)

