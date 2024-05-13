from openpyxl import load_workbook
import time
import logging

import requests
from main.main import get_name, get_screen_name

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(levelname)s - %(message)s')


def get_comments(screen_name):
    token = 'vk1.a.byMJTaFR8uzQ2VOgF72GpGczOd0RnOu1YBVklpdL9Rnndd-5TSH1FGz94XMiFgw4b13TFUQNikYHk79VQ5jwJ7GHKIoVZb3No7t97wJZTlgj5iqirPrXCXikDQOuSewYbYUbwuMb7kth4YqsAC8pDxBE-ax68I0qYiEHhkFnumJo3HzsWxRgvfPKwMck6jl1IDxVnpZ_uTGQMAZa2Kl9Xg'
    version = 5.199
    domain = screen_name
    count = 2
    offset = 0
    comments = []
    thread_items_count = 10
    while offset < 2:                                                
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
    with open('comments.txt', 'w', newline='', encoding="utf-8") as file:
        for comment in data:
            if comment['text'] != '':
                file.write("%s\n" % comment['text'])
     

# url = "https://vk.com/ria"
# comments = get_comments(get_screen_name(get_name(url)))
# file_writer_comments(comments)                                       
