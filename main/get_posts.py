import requests
from main.main import get_name, get_screen_name
import json
import csv
import docx
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(levelname)s - %(message)s')

def get_posts_count(screen_name):
    token = 'vk1.a.byMJTaFR8uzQ2VOgF72GpGczOd0RnOu1YBVklpdL9Rnndd-5TSH1FGz94XMiFgw4b13TFUQNikYHk79VQ5jwJ7GHKIoVZb3No7t97wJZTlgj5iqirPrXCXikDQOuSewYbYUbwuMb7kth4YqsAC8pDxBE-ax68I0qYiEHhkFnumJo3HzsWxRgvfPKwMck6jl1IDxVnpZ_uTGQMAZa2Kl9Xg'
    version = 5.199
    owner_id = screen_name
    count = 1
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
    if posts_count > 100:
        count_count = 100
        while (offset+100) < posts_count:
            response = requests.get('https://api.vk.com/method/wall.get',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'owner_id': owner_id,
                                        'count': count_count,
                                        'offset': offset
                                    })
            print(response.json())
            data = response.json()['response']['items']
            offset += 100
            posts.extend(data)
        print(offset)
        count_count = posts_count - offset
        print(count_count)
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'owner_id': owner_id,
                                    'count': count_count,
                                    'offset': offset
                                })
        data = response.json()['response']['items']
        posts.extend(data)
        print(data)
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
        print(data)
    return posts

def make_json(data):
    texts = []
    for post in data:
        texts.append(post['text'])
    texts = [line.replace("\n", "") for line in texts]
    data = []
    for text in texts:
        data.append({"text": text})
    json_data = data
    return json_data


url_module_2 = 'http://localhost:8002/api'

def zapros(data):
    response = requests.post(url_module_2, data = json.dumps(data))
    if response.status_code == 202:
        token = response.json()['id']
    while (response.status_code != 200):
        response = requests.get(f'{url_module_2}/{token}')
        answers = response.json()
        return answers
    if (response.status_code != 200 & response.status_code != 200): 
        print(response.status_code)

def posts_txt(data):
    text = ''
    for answer in data:
        text += "\nTeкст поста:\n" + str(answer['text']) + "\nЗапрещенный контент найден?: " + str(answer['result'])
    return text


def posts_txt_with_id(data):
    text = ''
    for answer in data:
        text += "\nTeкст поста:\n" + str(answer['text']) + "\nЗапрещенный контент найден?: " + str(answer['result'])
    return text


    # with open('posts_with_id.txt', 'a', newline='', encoding="utf-8") as file:
    #     for post in data:
    #         post_id = "https://vk.com/wall" + str(post['from_id']) + "_" + str(post['id'])
    #         text = post_id + "\n" + post['text']
    #         text = text.strip()
    #         file.write("%s\n" % text)


def posts_csv(data):
    with open('posts.csv', 'w', newline='', encoding="utf-8-sig") as file:
        for post in data:
            writer = csv.writer(file)
            writer.writerow([post['text']])

def posts_csv_with_id(data):
    with open('posts_with_id.csv', 'w', newline='', encoding="utf-8-sig") as file:
        for post in data:
            post_id = "https://vk.com/wall" + str(post['from_id']) + "_" + str(post['id'])
            writer = csv.writer(file)
            writer.writerow([post_id, post['text']])

def posts_docx(data):
    doc = docx.Document()
    for post in data:
        doc.add_paragraph(post['text'])
        doc.save("posts.docx")

def posts_docx_with_id(data):
    doc = docx.Document()
    for post in data:
        post_id = "https://vk.com/wall" + str(post['from_id']) + "_" + str(post['id'])
        doc.add_paragraph([post_id, post['text']])
        doc.save("posts_with_id.docx")


