from django.shortcuts import render, redirect
from django.http import *


def welcome(request):
    return HttpResponse("Hello World!")


def gallery(request):
    return HttpResponse("Strona jeszcze nie istnieje, zajrzyj proszę za kilka dni :)")


def blog(request):
    if request.user.is_authenticated:
        return redirect('blog')
    else:
        return render(request, 'blog')