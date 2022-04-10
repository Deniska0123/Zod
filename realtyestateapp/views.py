from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render


from .models import Article, Comment


def index(request):
    latest_list = Article.objects.order_by('-pub_date')[:12]
    print(latest_list)
    return render(request, 'realtyestateapp\list.html', {'latest_list':latest_list})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
        print(a)
    except:
        raise Http404("Статья не найдена!")

    return render(request, 'realtyestateapp/detail.html', {'article':a})

def fire(request):
    latest_list = Article.objects.filter(title__in = ['СТРЕЛЕЦ','ЛЕВ','ОВЕН'])
    print(latest_list)
    return render(request, 'realtyestateapp\list.html', {'latest_list':latest_list})

def water(request):
    latest_list = Article.objects.filter(title__in = ['РАК', 'СКОРПИОН', 'РЫБЫ'])
    print(latest_list)
    return render(request, 'realtyestateapp\list.html', {'latest_list':latest_list})

def air(request):
    latest_list = Article.objects.filter(title__in = ['БЛИЗНЕЦЫ', 'ВЕСЫ', 'ВОДОЛЕЙ'])
    print(latest_list)
    return render(request, 'realtyestateapp\list.html', {'latest_list':latest_list})

def earth(request):
    latest_list = Article.objects.filter(title__in = ['ТЕЛЕЦ', 'ДЕВА', 'КОЗЕРОГ'])
    print(latest_list)
    return render(request, 'realtyestateapp\list.html', {'latest_list':latest_list})

def statia(request):
    latest_list = Article.objects.filter(text36__in = ['Статья'])
    print(latest_list)
    return render(request, 'realtyestateapp\list.html', {'latest_list':latest_list})