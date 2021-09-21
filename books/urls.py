from django.contrib import admin
from django.urls import include, path

from .views import book_list_view, book_detail_view

app_name = 'books'

urlpatterns = [
    path('', book_list_view, name='books-list'),
    path('<int:id>/', book_detail_view, name='book-detail'),
]