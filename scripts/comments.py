from openpyxl import load_workbook
import time

import requests
from main import get_name, get_screen_name

def get_comments(screen_name):
    token = 'vk1.a.byMJTaFR8uzQ2VOgF72GpGczOd0RnOu1YBVklpdL9Rnndd-5TSH1FGz94XMiFgw4b13TFUQNikYHk79VQ5jwJ7GHKIoVZb3No7t97wJZTlgj5iqirPrXCXikDQOuSewYbYUbwuMb7kth4YqsAC8pDxBE-ax68I0qYiEHhkFnumJo3HzsWxRgvfPKwMck6jl1IDxVnpZ_uTGQMAZa2Kl9Xg'
    version = 5.199
    domain = screen_name
    count = 1
    offset = 2
    comments = []
    thread_items_count = 10
    while offset < 10:                                                  #комменты к первым 50 постам (можно больше)
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'offset': offset,
                                    'count': count
                                })
        offset += 1
        posts = response.json()['response']['items']
        time.sleep(0.5)
        for post in posts:
            posts_id = post['id']
            comments_count = post['comments']['count']
            response = requests.get('https://api.vk.com/method/wall.getComments',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'owner_id': screen_name,
                                        'post_id': posts_id,
                                        'count': comments_count,
                                        "thread_items_count": thread_items_count
                                    })
            data = response.json()['response']['items']
            comments.extend(data)
    return comments


def file_writer_comments(data):
    fn = 'comments.xlsx'
    wb = load_workbook(fn)
    ws = wb['data']
    for comment in data:
        ws.append([comment['text']])
    wb.save(fn)
    wb.close()

# def file_writer_comments(data):                                                  #можно убрать csv
#     with open('comments.txt', 'w', newline='', encoding="utf-8") as file:
#         write = csv.writer(file)
#         for comment in data:
#             write.writerow((comment['from_id'], comment['text']))       #обработка тредов и пустых комментов

url = "https://vk.com/public22822305"
comments = get_comments(get_screen_name(get_name(url)))
file_writer_comments(comments)                                       #удалить пустые комменты
