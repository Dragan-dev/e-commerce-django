from django.contrib.auth.decorators import login_required
from random import randint
import random

from django.http import  Http404
from django.shortcuts import redirect, render
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
    query = request.GET.get('q')
    qs = Article.objects.search(query = query)
    context = {
        "object_list": qs
    }
    return render(request, "articles/search.html", context)
    



def article_detail_view(request, slug=None):
    article_object = None
    if slug is not None:
        try:
            article_object = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_object = Article.objects.filter(slug=slug).first()
        except:
            raise Http404

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
        return redirect(article_object.get_absolute_url())
    return render(request, "articles/create.html", context)
