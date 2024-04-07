from django.shortcuts import render
from django.views import View
from .models import Book, Author


class LandingPageView(View):
    def get(self, request):
        return render(request, "index.html")


class BookView(View):
    def get(self, request):
        search = request.GET.get("search_book")
        if not search:
            books = Book.objects.all()
            context = {
                "books": books,
                "search_book": search
            }
            return render(request, "book.html", context)

        else:
            books = Book.objects.filter(title__icontains=search)
            if books:
                context = {
                    "books": books,
                    "search_book": search
                }
                return render(request, "book.html", context)
            else:
                return render(request, "book.html")


class AboutBookView(View):
    def get(self, request, id):
        book = Book.objects.get(pk=id)
        return render(request, "full_data_book.html", {"book":book})
