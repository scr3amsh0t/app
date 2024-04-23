from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from main import account_info, posts, comments


def index(request):
    context = {
        'title' : 'Поиск запрещенного контента'
        }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title' : 'Поиск запрещеннного контента'
        }
    return render(request, 'main/about.html', context) 

def groups(request):
    context = {
        'title' : 'Поиск запрещеннного контента'
        }
    return render(request, 'main/groups.html', context) 

def account(request):
    context = {
        'title' : 'Поиск запрещеннного контента'
        }
    return render(request, 'main/account.html', context) 

def handle_account_info(request):
    if request.method == 'GET':
        data = request.GET
        print(data)
        input = data.get('textInput')
        print(input)
        info = account_info.get_account_info(account_info.get_screen_name(account_info.get_name(input)))
        result = account_info.file_writer_account(info)
        print(info)
        return JsonResponse({'result': result})

    return JsonResponse({'error': 'Invalid request'})

def handle_posts(request):
    if request.method == 'POST':
        data = request.POST
        input = data.get('input', None)
        result = posts.get_posts_count(input)
        return JsonResponse({'result': result})

    return JsonResponse({'error': 'Invalid request'})


def handle_comments(request):
    if request.method == 'POST':
        data = request.POST
        input = data.get('input', None)
        result = comments.get_comments(input)
        return JsonResponse({'result': result})
    
    return JsonResponse({'error': 'Invalid request'})
