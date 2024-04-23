from django.http import HttpResponse
from django.shortcuts import render
import scripts.account_info

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
