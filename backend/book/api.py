from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *


# router = DefaultRouter()
# router.register(r'papa/', PapaViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('book', AllBooksView.as_view()),
    path('book/<int:id>', BookView.as_view()),
]