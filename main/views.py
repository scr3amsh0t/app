from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from main import account_info, posts, comments, user_subscribitions, group_members


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

def handle_user_subs(request):
    if request.method == 'GET':
        data = request.GET
        input = data.get('textInput')
        name = user_subscribitions.get_screen_name(user_subscribitions.get_name(input))
        number = user_subscribitions.get_number_of_subscriptions(name)
        subs = user_subscribitions.get_user_subscriptions(name, number)
        result = user_subscribitions.file_writer(subs)
        return JsonResponse({'result': result})

    return JsonResponse({'error': 'Invalid request'})


def handle_posts(request):
    if request.method == 'GET':
        data = request.GET
        input = data.get('textInput')
        screen_name = posts.get_screen_name(posts.get_name(input))
        posts_count = posts.get_posts_count(screen_name)
        result = posts.file_writer_posts(posts.get_posts(screen_name, posts_count))
        return JsonResponse({'result': result})

    return JsonResponse({'error': 'Invalid request'})


def handle_comments(request):
    if request.method == 'GET':
        data = request.GET
        input = data.get('textInput')
        comms = comments.get_comments(comments.get_screen_name(comments.get_name(input)))
        result = comments.file_writer_comments(comms)
        return JsonResponse({'result': result})
    
    return JsonResponse({'error': 'Invalid request'})

def handle_group_members(request):
    if request.method == 'GET':
        data = request.GET
        input = data.get('textInput')
        name = group_members.get_screen_name(group_members.get_name(input))
        count = group_members.get_group_members_count(name)
        members = group_members.get_group_members(name, count)
        result = group_members.file_writer_members(members)
        return JsonResponse({'result': result})
    
    return JsonResponse({'error': 'Invalid request'})