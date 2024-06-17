from io import BytesIO
from django.http import HttpResponse
from django.http import FileResponse
from django.shortcuts import render
from main import get_comments, get_posts
from django.core.mail import EmailMessage
import os
from django.views.decorators.http import require_POST
from main.forms import EmailPostForm


def index(request):
    context = {
        'title': 'Поиск запрещенного контента'
    }
    return render(request, 'main/index.html', context)


def contact(request):
    context = {
        'title': 'Поиск запрещенного контента'
    }
    return render(request, 'main/contact.html', context)


def posts(request):
    context = {
        'title': 'Поиск запрещенного контента'
    }
    return render(request, 'main/posts.html', context)


def comments(request):
    context = {
        'title': 'Поиск запрещенного контента'
    }
    return render(request, 'main/comments.html', context)


def handler_posts(request):
    try:
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
                if check3 == 'on':
                    content = get_posts.posts_csv_with_id(get_posts.zapros(json_text), posts)
                    with open(content, 'rb') as f:
                        a = BytesIO(f.read())
                        response = FileResponse(a, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                        response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(content)
                    os.remove(content)   
                if check4 == 'on':
                    content = get_posts.posts_docx_with_id(get_posts.zapros(json_text), posts)
                    with open(content, 'rb') as f:
                        a = BytesIO(f.read())
                        response = FileResponse(a, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                        response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(content)
                    os.remove(content)
            else:
                if check2 == 'on':
                    content = get_posts.posts_txt(get_posts.zapros(json_text))
                    response = HttpResponse(content, content_type='application/octet-stream')
                    response['Content-Disposition'] = 'attachment; filename="posts.txt"'
                if check3 == 'on':
                    content = get_posts.posts_csv(get_posts.zapros(json_text))
                    with open(content, 'rb') as f:
                        a = BytesIO(f.read())
                        response = FileResponse(a, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                        response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(content)
                    os.remove(content)
                if check4 == 'on':
                    content = get_posts.posts_docx(get_posts.zapros(json_text))
                    with open(content, 'rb') as f:
                        a = BytesIO(f.read())
                        response = FileResponse(a, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                        response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(content)
                    os.remove(content)
        return response
    except TypeError:
        with open("errors.txt", "w") as f:
            f.write("Произошла ошибка. Проверьте правильность введенного URL.")
            f.close
        with open("errors.txt", "rb") as f:
            a = BytesIO(f.read())
            response = FileResponse(a, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename="errors.txt"'
        os.remove("errors.txt")
        return response


def handler_comments(request):
    try:
        if request.method == 'POST':
            data = request.POST
            input = data.get('textInput')
            points = data.get('points')
            radio1 = data.get('radio1')
            radio2 = data.get('radio2')
            check3 = data.get('check3')
            check4 = data.get('check4')
            check5 = data.get('check5')
            comms = get_comments.get_comments(get_comments.get_screen_name(get_comments.get_name(input)), points)
            json_text = get_comments.make_json(comms)
            if radio1 == 'on':
                if check3 == 'on':
                    comm_id = get_comments.make_comment_id_json(comms)
                    content = get_comments.comments_txt_with_comm_id(get_comments.zapros(json_text), comms, comm_id)
                    response = HttpResponse(content, content_type='application/octet-stream')
                    response['Content-Disposition'] = 'attachment; filename="comments_with_id.txt"'
                if check4 == 'on':
                    from_id = get_comments.make_id_json(comms)
                    content = get_comments.comments_csv_with_id(get_comments.zapros(json_text), from_id)
                    with open(content, 'rb') as f:
                        a = BytesIO(f.read())
                        response = FileResponse(a, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                        response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(content)
                    os.remove(content)
                if check5 == 'on':
                    from_id = get_comments.make_id_json(comms)
                    content = get_comments.comments_docx_with_id(get_comments.zapros(json_text), from_id)
                    with open(content, 'rb') as f:
                        a = BytesIO(f.read())
                        response = FileResponse(a, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                        response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(content)  
                    os.remove(content) 
            if radio2 == 'on':
                if check3 == 'on':
                    from_id = get_comments.make_id_json(comms)
                    content = get_comments.comments_txt_with_id(get_comments.zapros(json_text), from_id)
                    response = HttpResponse(content, content_type='application/octet-stream')
                    response['Content-Disposition'] = 'attachment; filename="comments_with_author_id.txt"'
                if check4 == 'on':
                    from_id = get_comments.make_id_json(comms)
                    content = get_comments.comments_csv_with_id(get_comments.zapros(json_text), from_id)
                    with open(content, 'rb') as f:
                        a = BytesIO(f.read())
                        response = FileResponse(a, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                        response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(content)
                    os.remove(content)
                if check5 == 'on':
                    from_id = get_comments.make_id_json(comms)
                    content = get_comments.comments_docx_with_id(get_comments.zapros(json_text), from_id)
                    with open(content, 'rb') as f:
                        a = BytesIO(f.read())
                        response = FileResponse(a, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                        response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(content)  
                    os.remove(content) 
            # else:
            #     if check3 == 'on':
            #         content = get_comments.comments_txt(get_comments.zapros(json_text))
            #         response = HttpResponse(content, content_type='application/octet-stream')
            #         response['Content-Disposition'] = 'attachment; filename="comments.txt"'
            #     if check4 == 'on':
            #         content = get_comments.comments_csv(get_comments.zapros(json_text))
            #         with open(content, 'rb') as f:
            #             a = BytesIO(f.read())
            #             response = FileResponse(a, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            #             response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(content)
            #         os.remove(content)  
            #     if check5 == 'on':
            #         content = get_comments.comments_docx(get_comments.zapros(json_text))
            #         with open(content, 'rb') as f:
            #             a = BytesIO(f.read())
            #             response = FileResponse(a, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            #             response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(content)  
            #         os.remove(content)        
        return response
    except TypeError:
        with open("errors.txt", "w") as f:
            f.write("Произошла ошибка. Проверьте правильность введенного URL.")
            f.close
        with open("errors.txt", "rb") as f:
            a = BytesIO(f.read())
            response = FileResponse(a, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename="errors.txt"'
        os.remove("errors.txt")
        return response


def post_share(request):
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['formTheme']
            body = f'''
                email для связи: {form.cleaned_data['formEmail']}
                
                Текст обращения:
                {form.cleaned_data['formMessage']}
            '''

            file = form.cleaned_data['formFile']

            email = EmailMessage(
                subject,
                body,
                'explicitdetectionapp@gmail.com',
                ['explicitdetectionapp@gmail.com']
            )
            if file:
                email.attach(file.name, file.read(), file.content_type)

            email.send()
            return success(request)
    return contact(request)


def success(request):
    context = {
        'title': 'Поиск запрещенного контента'
    }
    return render(request, 'main/success.html', context)
