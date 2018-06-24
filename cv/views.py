from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def home(request):
    return render(request, "cv/home.html")


@login_required
def home_authenticated(request):
    return render(request, "cv/home_authenticated.html")
