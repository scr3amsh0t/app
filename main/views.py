from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from main import get_comments, get_posts
from django.views.decorators.http import require_POST


def index(request):
    context = {
        'title' : 'Поиск запрещенного контента'
        }
    return render(request, 'main/index.html', context)

def contact(request):
    context = {
        'title' : 'Поиск запрещенного контента'
        }
    return render(request, 'main/contact.html', context) 

def posts(request):
    context = {
        'title' : 'Поиск запрещенного контента'
        }
    return render(request, 'main/posts.html', context) 

def comments(request):
    context = {
        'title' : 'Поиск запрещенного контента'
        }
    return render(request, 'main/comments.html', context) 


def handler_posts(request):
    if request.method == 'POST':
        data = request.POST
        points = data.get('points')
        radio1 = data.get('radio1')
        radio2 = data.get('radio2')
        check2 = data.get('check2')
        check3 = data.get('check3')
        check4 = data.get('check4')
        input = data.get('textInput')
        screen_name = get_posts.get_screen_name(get_posts.get_name(input))
        posts_count = get_posts.get_posts_count(screen_name)
        if radio2 == 'on':
            points = posts_count
            print(points)
        print(points)
        if (int(points) < posts_count):
            posts = get_posts.get_posts(screen_name, int(points))
        else:
            posts = get_posts.get_posts(screen_name, posts_count)
        json_text = get_posts.make_json(posts)
        answer = get_posts.posts_txt(get_posts.zapros(json_text))
        content = answer
        response = HttpResponse(content, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="posts.txt"'
        return response
    return response


def handler_comments(request):
    if request.method == 'POST':
        data = request.POST
        input = data.get('textInput')
        # comms = get_comments.get_comments(get_comments.get_screen_name(get_comments.get_name(input)))
        # result = get_comments.comments_txt(comms)
        content = input
        print(content)
        response = HttpResponse(content, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="comments.txt"'
        return response
    return response


