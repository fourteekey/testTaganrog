from rest_framework import serializers

from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('id', 'image_link', 'name', 'price', 'description', 'publishing_house', 'publish_year',
                  'category', 'count', 'created', 'author',)
