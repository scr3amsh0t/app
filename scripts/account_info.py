import requests
from main import get_name, get_screen_name

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




def file_writer_account(data):                                                #можно убрать csv
    with open('account_info.txt', 'w', newline='', encoding="utf-8") as file:
        file.write("%s\n" % data)


url = "https://vk.com/scr3amsh0t"
info = get_account_info(get_screen_name(get_name(url)))
file_writer_account(info)
