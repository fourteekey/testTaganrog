from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class AllBooksView(APIView):
    def get(self, request, format=None):
        books = BookModel.objects.all()

        return Response(BookSerializer(books, many=True, context={"request": request}).data)


class BookView(APIView):
    def get(self, request, id, format=None):
        book = get_object_or_404(BookModel, id=id)

        return Response(BookSerializer(book).data)


# Render Template
def books(request):
    all_books = BookModel.objects.all()

    paginator = Paginator(all_books, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return render(request, 'book.html', {'page_title': 'Список книг', 'page_data': page})
