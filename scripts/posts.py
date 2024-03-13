from openpyxl import load_workbook
import requests
from main import get_name, get_screen_name

def get_posts_count(screen_name):
    token = 'vk1.a.byMJTaFR8uzQ2VOgF72GpGczOd0RnOu1YBVklpdL9Rnndd-5TSH1FGz94XMiFgw4b13TFUQNikYHk79VQ5jwJ7GHKIoVZb3No7t97wJZTlgj5iqirPrXCXikDQOuSewYbYUbwuMb7kth4YqsAC8pDxBE-ax68I0qYiEHhkFnumJo3HzsWxRgvfPKwMck6jl1IDxVnpZ_uTGQMAZa2Kl9Xg'
    version = 5.199
    owner_id = screen_name
    count = 1                                                       # узнаем количество постов в сообществе
    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'owner_id': owner_id,
                                'count': count
                            })
    posts_count = response.json()['response']['count']
    return posts_count


def get_posts(screen_name, posts_count):
    token = 'vk1.a.byMJTaFR8uzQ2VOgF72GpGczOd0RnOu1YBVklpdL9Rnndd-5TSH1FGz94XMiFgw4b13TFUQNikYHk79VQ5jwJ7GHKIoVZb3No7t97wJZTlgj5iqirPrXCXikDQOuSewYbYUbwuMb7kth4YqsAC8pDxBE-ax68I0qYiEHhkFnumJo3HzsWxRgvfPKwMck6jl1IDxVnpZ_uTGQMAZa2Kl9Xg'
    version = 5.199
    owner_id = screen_name
    offset = 0
    posts = []
    if posts_count > 100:                                                # поправить реализацию, выдает результат кратный 100 (вроде починил)
        count_count = 100                                                # импортируются все посты группы
        while offset < posts_count:
            response = requests.get('https://api.vk.com/method/wall.get',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'owner_id': owner_id,
                                        'count': count_count,
                                        'offset': offset
                                    })
            data = response.json()['response']['items']
            offset += 100
            posts.extend(data)
    else:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'owner_id': owner_id,
                                    'count': posts_count,
                                    'offset': offset
                                })
        data = response.json()['response']['items']
        posts.extend(data)
    return posts


# def file_writer_posts(data):                                                #можно убрать csv
#     with open('posts.xlsx', 'a', newline='', encoding="utf-8") as file:
#         for post in data:
#             file.write("%s\n" % post['text'])

def file_writer_posts(data):
    fn = 'posts.xlsx'
    wb = load_workbook(fn)
    ws = wb['data']
    for post in data:
        ws.append([post['text']])
    wb.save(fn)
    wb.close()


url = "https://vk.com/bnethom"                                             #input
get_name(url)
screen_name = get_screen_name(get_name(url))
posts_count = get_posts_count(screen_name)
posts = get_posts(screen_name, 70)
file_writer_posts(posts)