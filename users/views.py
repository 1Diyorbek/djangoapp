from django.shortcuts import render
from django.http import HttpResponse


def greeting(request):
    return render(request, "greeting.html")


def image(request):
    return render(request, "image.html")
