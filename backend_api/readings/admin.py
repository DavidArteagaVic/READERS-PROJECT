from django.contrib import admin
from .models import books

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'published_year', 'isbn', 'publisher', 'pages', 'language', 'description', 'cover_image', 'status')

admin.site.register(books, BookAdmin)
