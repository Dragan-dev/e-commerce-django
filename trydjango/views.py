from django.contrib.auth.decorators import login_required
from random import randint
import random
from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article
from articles.forms import ArticleForm
from . import views


def home(request):
    rand_id = random.randint(1, 3)
    object = Article.objects.get(id=rand_id)
    article_queryset = Article.objects.all()

    context = {
        "object": object,
        "content": object.content,
        "title": object.title,
        "id": object.id,
        "object_list": article_queryset,
    }

    return render(request, 'home.html', context)


def articles_detail_view(request, id):
    context = {
        "object": None,
    }
    return render(request, 'articles/detail.html', context)


def article_search_view(request):
    query_dict = request.GET
    # query=query_dict.get("q") # <input type = 'text' name='q'>
    try:
        query = int(query_dict.get("q"))
    except:
        query = None
    article_object = None
    if query is not None:
        article_object = Article.objects.get(id=query)

    context = {
        "object": article_object
    }
    return render(request, "articles/search.html", context=context)


def article_detail_view(request, id=None):
    article_object = None
    if id is not None:
        article_object = Article.objects.get(id=id)
    context = {
        "object": article_object
    }
    return render(request, "articles/detail.html", context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        #context['object'] = article_object
        #context['created'] = True
    return render(request, "articles/create.html", context)


# def article_create_view(request):
#    # print(request.POST)
#    form = ArticleForm()
#    print(dir(form))
#    context = {
#        "form": form
#    }
#    if request.method == "POST":
#        form = ArticleForm(request.POST)
#          context['form'] = form
#       
#        if form.is_valid():
#            title = form.cleaned_data.get("title")
#            content = form.cleaned_data.get("content")
#            print(title, content)
#            article_object = Article.objects.create(
#                title=title, content=content)
#            context['object'] = article_object
#            context['created'] = True
#    return render(request, "articles/create.html", context)
#
