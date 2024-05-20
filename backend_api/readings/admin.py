from django.contrib import admin
from .models import books

admin.site.register(books)
# Register your models here.

class booksFields(admin.ModelAdmin):
    list_display = ('title','author','genre','published_year',
                    'isbn','publisher','pages','lenguage',
                    'description','over_image_url')
    
    
admin.site.register(books)