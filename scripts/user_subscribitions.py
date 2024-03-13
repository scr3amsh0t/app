import requests
from main import get_name, get_screen_name


def get_number_of_subscriptions(screen_name):
    token = 'vk1.a.SyTH5D_MSxLRQ5M5pyMAouDxVL-y2NGg_4eBnrISInDEBKYQ8weg6gn8vj7cb0TZ7gnqJ7qAj3hbejLMcbjehXbfHCiCUWD_32mRpUfGDQnvzvhFNNXU0xjjI-Saa86SiuWQ0yxPRP73B8JsXOUlp0x1Y4vg-hPRbiJPVkd0pBrDX5PeuQfasp863wLZt9rse3_tzwVZzQauIAZLZABqkw'
    version = 5.199
    user_id = screen_name
    response = requests.get('https://api.vk.com/method/users.getSubscriptions',
                            params={
                                'access_token': token,
                                'v': version,
                                'user_id': user_id,
                            })
    group_numbers = response.json()['response']['groups']['count']
    return group_numbers

def get_user_subscriptions(screen_name, group_numbers):
    token = 'vk1.a.SyTH5D_MSxLRQ5M5pyMAouDxVL-y2NGg_4eBnrISInDEBKYQ8weg6gn8vj7cb0TZ7gnqJ7qAj3hbejLMcbjehXbfHCiCUWD_32mRpUfGDQnvzvhFNNXU0xjjI-Saa86SiuWQ0yxPRP73B8JsXOUlp0x1Y4vg-hPRbiJPVkd0pBrDX5PeuQfasp863wLZt9rse3_tzwVZzQauIAZLZABqkw'
    version = 5.199
    user_id = screen_name
    count = group_numbers
    offset = 0
    users = []
    if count > 200:
        count_count = 200
        while offset < count:
            response = requests.get('https://api.vk.com/method/users.getSubscriptions',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'user_id': user_id,
                                        'extended': 1,
                                        'count': count_count,
                                        'offset': offset
                                    })
            group_info = response.json()['response']['items']
            users.extend(group_info)
            offset += 200
    else:
        response = requests.get('https://api.vk.com/method/users.getSubscriptions',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'user_id': user_id,
                                    'extended': 1,
                                    'count': count
                                })
        group_info = response.json()['response']['items']
        users.extend(group_info)
    return users

def file_writer(data):                                                #можно убрать csv
    with open('user_subscriptions.txt', 'w', newline='', encoding="utf-8") as file:
        for info in data:
            if (info['type'] == 'page' or info['type'] == 'group'):
                info = ["vk.com/club%s" % info['id'], info['name']]
                file.write("%s\n" % info)

url = "https://vk.com/aweipo"
group_number = get_number_of_subscriptions(get_screen_name(get_name(url)))
groups = get_user_subscriptions(get_screen_name(get_name(url)), group_number)
file_writer(groups)