from rest_framework import serializers

from .models import *
from book.models import *
from book.serializers import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('id', 'full_name', 'description', 'country', 'birth_day',)

    def get_author_book(self, author_id):
        books = BookModel.objects.filter(author=author_id)
        serializer_books = BookSerializer(books, many=True).data
        author = AuthorModel.objects.get(id=author_id)
        res = {'id': author.id, 'full_name': author.full_name, 'description': author.description,
               'country': author.country, 'birth_day': author.birth_day, 'books': serializer_books}

        return res
