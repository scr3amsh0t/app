from django.http import HttpResponse, HttpResponseNotFound
from django.http import FileResponse
from django.shortcuts import render
from main import get_comments, get_posts
import os
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
        radio2 = data.get('radio2')
        check1 = data.get('check1')
        check2 = data.get('check2')
        check3 = data.get('check3')
        check4 = data.get('check4')
        input = data.get('textInput')
        screen_name = get_posts.get_screen_name(get_posts.get_name(input))
        posts_count = get_posts.get_posts_count(screen_name)
        if radio2 == 'on':
            points = posts_count
        if (int(points) < posts_count):
            posts = get_posts.get_posts(screen_name, int(points))
        else:
            posts = get_posts.get_posts(screen_name, posts_count)
        json_text = get_posts.make_json(posts)
        if check1 == 'on':
            if check2 == 'on':
                content = get_posts.posts_txt_with_id(get_posts.zapros(json_text), posts)
                response = HttpResponse(content, content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename="posts_id.txt"'
        else:
            if check2 == 'on':
                content = get_posts.posts_txt(get_posts.zapros(json_text))
                response = HttpResponse(content, content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename="posts.txt"'
            if check4 == 'on':
                content = get_posts.posts_docx(get_posts.zapros(json_text))
                with open(content, 'rb') as f:
                    response = HttpResponse(f.read(), content_type='application/octet-stream')
                    response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(content)
    return response
        


def handler_comments(request):
    if request.method == 'POST':
        data = request.POST
        input = data.get('textInput')
        points = data.get('points')
        check3 = data.get('check3')
        check4 = data.get('check4')
        check5 = data.get('check5')
        comms = get_comments.get_comments(get_comments.get_screen_name(get_comments.get_name(input)), points)
        json_text = get_comments.make_json(comms)
        if check3 == 'on':
            content = get_comments.comments_txt(get_comments.zapros(json_text))
            response = HttpResponse(content, content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename="comments.txt"'
    return response


