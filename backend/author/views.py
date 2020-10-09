from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class AllAuthorsView(APIView):
    def get(self, request, format=None):
        author = AuthorModel.objects.filter()

        return Response(AuthorSerializer(author, many=True, context={"request": request}).data)


class AuthorView(APIView):
    def get(self, request, id, format=None):
        return Response(AuthorSerializer().get_author_book(author_id=id))


# Render Template
def author_page(request, id):
    # print('AUTHOR PAGE', request.GET.get('id', None))
    # print('ID: ', id)
    # author = get_object_or_404(AuthorModel, id=id)
    author = AuthorSerializer().get_author_book(author_id=id)
    return render(request, 'author_card.html', {'author': author})
