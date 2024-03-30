from django.shortcuts import render


def greeting(request):
    return render(request, "greeting.html")


def image(request):
    return render(request, "image.html")
