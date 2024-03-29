from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "index.html")


def after_home(request):
    return render(request, "after_home.html")
