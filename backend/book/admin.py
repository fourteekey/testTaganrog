from django.contrib import admin
from .models import *


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('image_link', 'name', 'price', 'description', 'publishing_house', 'publish_year', 'category',
                    'count', 'created', 'get_author_list')


    def get_author_list(self, obj):
        objs = obj.author.all()
        res = ''
        if objs:
            for data in objs:
                res += str(data) + ',\n'
        else:
            res = ' — '

        return res


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active',)


@admin.register(Publishing_HouseModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active',)
