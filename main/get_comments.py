import time
import logging
import json
import csv
import docx
import requests

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(levelname)s - %(message)s')


def get_comments(screen_name,posts_count):
    token = 'vk1.a.byMJTaFR8uzQ2VOgF72GpGczOd0RnOu1YBVklpdL9Rnndd-5TSH1FGz94XMiFgw4b13TFUQNikYHk79VQ5jwJ7GHKIoVZb3No7t97wJZTlgj5iqirPrXCXikDQOuSewYbYUbwuMb7kth4YqsAC8pDxBE-ax68I0qYiEHhkFnumJo3HzsWxRgvfPKwMck6jl1IDxVnpZ_uTGQMAZa2Kl9Xg'
    version = 5.199
    domain = screen_name
    count = 1
    offset = 0
    comments = []
    thread_items_count = 10
    while offset < int(posts_count):
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

def make_json(data):
    texts = []
    for comment in data:
        if comment['text'] != '':
            texts.append(comment['text'])
        threads = comment['thread']['items']
        for thread in threads:
                if thread['text'] != '':
                    texts.append(thread['text'])
    texts = [line.replace("\n", "") for line in texts]
    data = []
    for text in texts:
        data.append({"text": text})
    return data


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
     
def comments_txt(data):
    text = ''
    i = 1
    for answer in data:
        text += "Teкст комментария " + str(i) + ":\n" + str(answer['text']) + "\nЗапрещенный контент найден?: " + str(answer['result'] + "\n")
        i+=1
    return text


def comments_txt_with_id(data):
    with open('comments_with_id.txt', 'a', newline='', encoding="utf-8") as file:
        for comment in data:
            post_id = "https://vk.com/wall" + str(comment['from_id']) + "_" + str(comment['id'])
            text = post_id + "\n" + comment['text']
            text = text.strip()
            file.write("%s\n" % text)


def comments_csv(data):
    with open('comments.csv', 'w', newline='', encoding="utf-8-sig") as file:
        for comment in data:
            writer = csv.writer(file)
            writer.writerow([comment['text']])

def comments_csv_with_id(data):
    with open('comments_with_id.csv', 'w', newline='', encoding="utf-8-sig") as file:
        for comment in data:
            comment_id = "https://vk.com/wall" + str(comment['from_id']) + "_" + str(comment['id'])
            writer = csv.writer(file)
            writer.writerow([comment_id, comment['text']])

def comments_docx(data):
    doc = docx.Document()
    for comment in data:
        doc.add_paragraph(comment['text'])
        doc.save("comments.docx")

def comments_docx_with_id(data):
    doc = docx.Document()
    for comment in data:
        comment_id = "https://vk.com/wall" + str(comment['from_id']) + "_" + str(comment['id'])
        doc.add_paragraph([comment_id, comment['text']])
        doc.save("comments_with_id.docx")
