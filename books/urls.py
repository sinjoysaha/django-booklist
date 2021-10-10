from django.contrib import admin
from django.urls import include, path

from .views import (book_list_view, 
                    book_detail_view, 
                    book_create_view, 
                    book_update_view,
                    book_delete_view)

app_name = 'books'

urlpatterns = [
    path('', book_list_view, name='books-list'),
    path('<int:id>/', book_detail_view, name='book-detail'),
    path('create/', book_create_view, name="book-create"),
    path('<int:id>/update/', book_update_view, name="book-update"),
    path('<int:id>/delete/', book_delete_view, name="book-delete"),
]