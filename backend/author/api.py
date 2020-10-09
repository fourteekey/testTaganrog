from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *


# router = DefaultRouter()
# router.register(r'papa/', PapaViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('author', AllAuthorsView.as_view()),
    path('author/<int:id>', AuthorView.as_view()),
]