from django.contrib import admin
from .models import User, Address
from import_export.admin import ImportExportModelAdmin


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ("id", "first_name", "last_name", "image", "username", "status", "age", "address")
    list_display_links = ("id", "first_name", "last_name", "image", "username", "status", "age", "address")
    search_fields = ('id', 'first_name', "last_name")
    search_help_text = f'write only id, first_name, lastname'
    ordering = ('first_name', 'last_name', 'id')
    autocomplete_fields = ["address"]


@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ('id', 'title')
    search_help_text = f'write only id or title'
    ordering = ('title', )
