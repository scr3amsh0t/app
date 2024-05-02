import requests
import time
from main.main import get_name, get_screen_name

def get_group_members_count(screen_name):
    token = 'vk1.a.byMJTaFR8uzQ2VOgF72GpGczOd0RnOu1YBVklpdL9Rnndd-5TSH1FGz94XMiFgw4b13TFUQNikYHk79VQ5jwJ7GHKIoVZb3No7t97wJZTlgj5iqirPrXCXikDQOuSewYbYUbwuMb7kth4YqsAC8pDxBE-ax68I0qYiEHhkFnumJo3HzsWxRgvfPKwMck6jl1IDxVnpZ_uTGQMAZa2Kl9Xg'
    version = 5.199
    group_id = screen_name
    response = requests.get('https://api.vk.com/method/groups.getById',
                            params={
                                'access_token': token,
                                'v': version,
                                'group_id': -group_id,                     #указывается положительное значение id
                                'fields': 'members_count'
                            })
    group_info = response.json()['response']['groups']
    for members in group_info:
        members_count = members['members_count']
    return members_count

def get_group_members(screen_name, members_count):
    token = 'vk1.a.byMJTaFR8uzQ2VOgF72GpGczOd0RnOu1YBVklpdL9Rnndd-5TSH1FGz94XMiFgw4b13TFUQNikYHk79VQ5jwJ7GHKIoVZb3No7t97wJZTlgj5iqirPrXCXikDQOuSewYbYUbwuMb7kth4YqsAC8pDxBE-ax68I0qYiEHhkFnumJo3HzsWxRgvfPKwMck6jl1IDxVnpZ_uTGQMAZa2Kl9Xg'
    version = 5.199
    group_id = screen_name
    count = members_count
    offset = 0
    members = []
    if count > 1000:
        count_count = 1000
        while offset < count:
            response = requests.get('https://api.vk.com/method/groups.getMembers',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'group_id': -group_id,                   #положительное значение
                                        'count': count_count,
                                        'offset': offset
                                    })
            data = response.json()['response']['items']
            members.extend(data)
            offset += 1000
            time.sleep(1)
    else:
        response = requests.get('https://api.vk.com/method/groups.getMembers',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'group_id': -group_id,                        # положительное значение
                                    'count': count
                                })
        data = response.json()['response']['items']
        members.extend(data)
    return members

def file_writer_members(data):
    with open('members.txt', 'w', newline='', encoding="utf-8") as file:
        for item in data:
            file.write("vk.com/id%s\n" % item)

url = "https://vk.com/miet_one"

members_count = get_group_members_count(get_screen_name(get_name(url)))
members = get_group_members(get_screen_name(get_name(url)), members_count)
file_writer_members(members)