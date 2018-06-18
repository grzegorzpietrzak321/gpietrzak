from django.shortcuts import render
from blog.models import Article
from django.contrib.auth.models import User


def home(request):
    all_articles = list(Article.objects.all())
    username = User.first_name

    return render(request, "blog/home.html", {'articles': all_articles}, {'user': username})
