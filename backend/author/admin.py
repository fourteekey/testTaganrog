from django.contrib import admin
from .models import *


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'description', 'country', 'birth_day',)


@admin.register(CountryModel)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active',)
