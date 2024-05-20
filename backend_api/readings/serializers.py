from rest_framework import serializers
from readings.models import books

class BookSerializer(serializers.ModelSerializer):
    class Meta: 
        Model = books
        field  = [
            'title',
            'author',
            'genre',
            'published_year',
            'isbn',
            'publisher',
            'pages',
            'lenguage',
            'description',
            'cover_image',
            'status'
        ] 