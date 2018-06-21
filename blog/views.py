from django.shortcuts import render
from blog.models import Article
from django.contrib.auth.models import User


def home(request):
    posted_articles = list(Article.objects.all())
    username = User.first_name

    return render(request, "blog/home.html",
                  {'articles': posted_articles}, {'user': username})


def getall(request):
    all_articles = list(Article.objects.all())
    username = User.first_name

    return render(request, "blog/home.html",
                  {'articles': all_articles}, {'user': username})