from django.contrib import admin
from .models import Book, Author, BookingBook, Comment
from import_export.admin import ImportExportModelAdmin

@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("id", "first_name", "last_name", "birt_date")
    list_display_links = ("id", "first_name", "last_name", "birt_date")
    search_fields = ("id", "first_name")
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('first_name', 'id')


@admin.register(Book)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("id", "title", "description", "price", "author")
    list_display_links = ("id", "title", "description", "price", "author")
    search_fields = ("id", "title")
    search_help_text = f"search in: {' or '.join(search_fields)}"
    ordering = ('title', '-price', 'id')
    autocomplete_fields = ["author"]


@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ("id", "user", "book", "text")
    list_display_links = ("id", "user", "book", "text")
    search_fields = ("id", "text")
    search_help_text = f"search in: {' or ' .join(search_fields)}"
    ordering = ("id", )
    autocomplete_fields = ["user", "book"]


@admin.register(BookingBook)
class BookingBookAdmin(ImportExportModelAdmin):
    list_display = ["take_date", "returned_book"]
    list_display_links = ["take_date", "returned_book"]
    search_fields = ("take_date", )
    search_help_text = "search in: take_date"
    ordering = ("returned_book", )
    autocomplete_fields = ["user", "book"]
