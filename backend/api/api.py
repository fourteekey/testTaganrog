from django.urls import path, include


urlpatterns = [
    # path('', include('app_example.api')),
    path('', include('book.api')),
    path('', include('author.api')),
]
